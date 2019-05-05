from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'apps.common'
    verbose_name = u"管理"

    def ready(self):
        import apps.common.signals # signals.py路径
