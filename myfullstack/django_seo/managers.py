from django.db.models import QuerySet


class GlobalManager(QuerySet):
    def get_latest_version(self):
        try:
            queryset = self.all()
            return queryset.latest('created_on')
        except:
            return None
