class GlobalMixins:
    authentication_classes = []
    permission_classes = []


class GlobalAPIMixins:
    @classmethod
    def get_extra_actions(self, **kwargs):
        return []

