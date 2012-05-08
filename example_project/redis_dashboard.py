from admin_tools.dashboard.dashboards import DefaultIndexDashboard
from redis_stats.admin_tools_redis import RedisStatsModule


class CustomIndexDashboard(DefaultIndexDashboard):
    """
    Custom index dashboard with redis module
    """
    def init_with_context(self, context):
        super(CustomIndexDashboard, self).init_with_context(context)
        self.children.append(RedisStatsModule())
