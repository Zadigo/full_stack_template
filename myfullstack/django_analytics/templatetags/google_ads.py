from django.template import Library

register = Library()


# @register.inclusion_tag('google/ads/tag.html')
# def remarketing(tag=None):
#     """Implements Google Analytics"""
#     tag = load_default(key='google_ads', tag=tag)
#     return {'google_ads_id': tag}


@register.tag('google/ads/conversion_telephone.html')
def conversion_telephone(conversion_id, conversion_label, telephone):
    """Adds a conversion telephone tag that allows to
    track when the user clicks on a link that contains
    a telephone number to call the company"""
    return {
        'conversion_id': conversion_id,
        'conversion_label': conversion_label,
        'telephone': telephone
    }


@register.tag('google/ads/conversion.html')
def conversion(conversion_id, conversion_label):
    """Registers a conversion tag on a conversion
    page which allows to send a conversion to
    Google Ads"""
    return {
        'conversion_id': conversion_id,
        'conversion_label': conversion_label
    }
