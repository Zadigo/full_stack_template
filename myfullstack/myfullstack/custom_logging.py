import logging


class FailedRequestFilter(logging.Filter):
    """A custom logger for failed request"""

    def filter(self, record):
        result = super().filter(record)
        status_codes = [400, 401, 403, 404, 405, 500, 502, 503, 504]
        if record.status_code in status_codes:
            return all([result, True])
        return False
