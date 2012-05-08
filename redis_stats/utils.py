import ctypes
import os
import redis

class MemoryCheck():
    """Checks memory of a given system"""

    def __init__(self):

        if os.name == "posix":
            self.value = self.linuxRam()
        elif os.name == "nt":
            self.value = self.windowsRam()
        else:
            print "I only work with Win or Linux :P"

    def windowsRam(self):
        """Uses Windows API to check RAM in this OS"""
        kernel32 = ctypes.windll.kernel32
        c_ulong = ctypes.c_ulong
        class MEMORYSTATUS(ctypes.Structure):
            _fields_ = [
                ("dwLength", c_ulong),
                ("dwMemoryLoad", c_ulong),
                ("dwTotalPhys", c_ulong),
                ("dwAvailPhys", c_ulong),
                ("dwTotalPageFile", c_ulong),
                ("dwAvailPageFile", c_ulong),
                ("dwTotalVirtual", c_ulong),
                ("dwAvailVirtual", c_ulong)
            ]
        memoryStatus = MEMORYSTATUS()
        memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUS)
        kernel32.GlobalMemoryStatus(ctypes.byref(memoryStatus))

        return int(memoryStatus.dwTotalPhys/1024**2)

    def linuxRam(self):
        """Returns the RAM of a linux system"""
        totalMemory = os.popen("free -m").readlines()[1].split()[1]
        return int(totalMemory)

def get_redis_stats():
    full_info_dict = redis.Redis().info()
    full_info = full_info_dict.items()
    full_info.sort(key=lambda i: i[0])
    server_info = [(k,v) for k,v in full_info if not k.startswith('db')]
    db_info = [(k,v) for k,v in full_info if k.startswith('db')]

    cpu_percent = full_info_dict.get('used_cpu_sys', 0)

    ram_size = MemoryCheck().value
    ram_percent = float(full_info_dict.get('used_memory_rss', 0)) / 1000000 / ram_size * 100

    print ram_percent

    return {
        'server_info': server_info,
        'db_info': db_info,
        'cpu_percent': cpu_percent,
        'ram_percent': ram_percent,
    }
