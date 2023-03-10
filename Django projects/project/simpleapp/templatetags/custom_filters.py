from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
    'rub': 'P',
    'usd': '$'
}

@register.filter()
def currency(value):
    """

    value:
    code:
    """
    postfix = CURRENCIES_SYMBOLS[code]
    return f'{value} {postfix}'
