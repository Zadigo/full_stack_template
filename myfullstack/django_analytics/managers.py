from django.db.models import QuerySet


class GlobalManager(QuerySet):
    def get_latest_version(self):
        """Returns the latest container based
        on the creation date"""
        try:
            queryset = self.all()
            return queryset.latest('created_on')
        except:
            return None

    def get_last_version(self):
        """Returns the last version based
        on the version number"""
        try:
            queryset = self.all()
            return queryset.last()
        except:
            return None
