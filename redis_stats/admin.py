from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from redis_stats.models import RedisStats
from redis_stats.utils import get_redis_stats

class RedisStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return render(request, 'redis_stats/admin/info.html', get_redis_stats())

    def get_model_perms(self, request):
        return {'change': True, 'add': False}

if not 'admin_tools.dashboard' in settings.INSTALLED_APPS:
    RedisStats._meta.abstract = False

    info = get_redis_stats()
    percentage = 'CPU: %.2f%% RAM: %.2f%%' % (info['cpu_percent'], info['ram_percent'])
    RedisStats._meta.verbose_name_plural = _('Redis stats %s') % percentage

    admin.site.register(RedisStats, RedisStatsAdmin)

