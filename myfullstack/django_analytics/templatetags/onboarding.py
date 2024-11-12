from django.template import Library

register = Library()


@register.inclusion_tag('appcues.html')
def appcues(account_id):
    return {'appcues_account_id': account_id}
