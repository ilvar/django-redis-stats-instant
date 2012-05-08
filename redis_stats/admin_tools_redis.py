from django.utils.translation import ugettext as _

from admin_tools.dashboard.modules import DashboardModule

from redis_stats.utils import get_redis_stats


class RedisStatsModule(DashboardModule):
    template = 'redis_stats/admin_tools/module.html'
    title = _('Redis stats')
    layout='inline',
    draggable=False,
    deletable=False,
    collapsible=False,

    def __init__(self, title=None, **kwargs):
        super(RedisStatsModule, self).__init__(title, **kwargs)
        info = get_redis_stats()
        self.children = [
            {'name': _('CPU'), 'percent': info['cpu_percent']},
            {'name': _('RAM'), 'percent': info['ram_percent']},
        ]
