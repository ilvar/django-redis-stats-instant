This little application just shows current Redis stats on Django's admin dashboard. Also supports django-admin-tools nicely.

Install
=======

1. Install with `pip install -e https+git://ilvar@github.com/ilvar/django-redis-stats-instant.git`
2. Add `'redis_stats'` to `INSTALLED_APPS` in your `settings`
3. If you're using [django-admin-tools](https://bitbucket.org/izi/django-admin-tools/wiki/Home)
    1. Just add Redis Stats module to your custom dashboard (or create a new one), as [provided in our example.](https://github.com/ilvar/django-redis-stats-instant/blob/master/example_project/redis_dashboard.py)
    2. Do not forget to add your custom dashboard to `settings`:
`ADMIN_TOOLS_INDEX_DASHBOARD = 'redis_dashboard.CustomIndexDashboard'`
5. That's it. With
[django-admin-tools](https://bitbucket.org/izi/django-admin-tools/wiki/Home)
you'll have a nice widget for the dashboard, for old-fashioned django
admin there will be not so nice but still reliable fake application section.

