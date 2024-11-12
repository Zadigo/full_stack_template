import re

from django_mobile import set_mobile_state

WIDE_USER_AGENTS = {
    "w3c ", "acs-", "alav", "alca", "amoi", "audi",
    "avan", "benq", "bird", "blac", "blaz", "brew",
    "cell", "cldc", "cmd-", "dang", "doco", "eric",
    "hipt", "inno", "ipaq", "java", "jigs", "kddi",
    "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
    "maui", "maxo", "midp", "mits", "mmef", "mobi",
    "mot-", "moto", "mwbp", "nec-", "newt", "noki",
    "xda",  "palm", "pana", "pant", "phil", "play",
    "port", "prox", "qwap", "sage", "sams", "sany",
    "sch-", "sec-", "send", "seri", "sgh-", "shar",
    "sie-", "siem", "smal", "smar", "sony", "sph-",
    "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
    "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
    "wapi", "wapp", "wapr", "webc", "winw", "xda-"
}

COMMON_USER_AGENTS = {
    'up.browser', 'up.link', 'mmp', 'symbian', 'smartphone', 'midp',
    'wap', 'phone', 'windows ce', 'pda', 'mobile', 'mini', 'palm',
    'netfront', 'opera mobi', 'android'
}

USER_AGENTS_EXCEPTIONS = {'ipad'}

# TODO: MIME type apparently used in mobiles ?
HTTP_ACCEPT_REGEX = re.compile(
    'application/vnd.wap.xhtml\\+xml',
    re.IGNORECASE
)


class DjangoMobileMiddleware:
    """A middleware for detecting if a request
    comes from a mobile or not"""

    def __init__(self, get_response):
        self.get_response = get_response

        self.common_user_agents_regex = re.compile(
            '(?:%s)' % '|'.join(COMMON_USER_AGENTS), re.IGNORECASE
        )
        self.wide_user_agents_regex = re.compile(
            '(?:%s)' % '|'.join(WIDE_USER_AGENTS), re.IGNORECASE
        )
        self.user_agents_exceptions_regex = re.compile(
            '(?:%s)' % '|'.join(USER_AGENTS_EXCEPTIONS), re.IGNORECASE
        )

    def __call__(self, request):
        is_mobile = False
        http_user_agent = request.META.get('HTTP_USER_AGENT', None)
        if http_user_agent is not None:
            # First, we'll test all the most
            # common mobile user agents
            if (self.common_user_agents_regex.search(http_user_agent) and
                    not self.user_agents_exceptions_regex.search(http_user_agent)):
                is_mobile = True
            else:
                # If we got nothing, test the HTTP_ACCEPT header
                http_accept = request.META.get('HTTP_ACCEPT', None)
                if http_accept is not None:
                    if HTTP_ACCEPT_REGEX.search(http_accept):
                        is_mobile = True

            # If we still do not have any match,
            # use a wider search for less common agents
            if not is_mobile:
                if self.wide_user_agents_regex.match(http_user_agent):
                    is_mobile = True

        set_mobile_state(is_mobile, request, persistent=True)
        response = self.get_response(request)
        return response
