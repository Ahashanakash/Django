from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter
def intcomma_every_three(value):
    """
    Adds commas every 3 digits (standard format).
    For example: 1234567.89 becomes 1,234,567.89
    """
    if value is None:
        return ''
    
    # Convert to string and handle decimal part
    str_value = str(value)
    
    # Split into integer and decimal parts
    if '.' in str_value:
        integer_part, decimal_part = str_value.split('.')
    else:
        integer_part = str_value
        decimal_part = ''
    
    # Add commas every 3 digits from right to left
    formatted_integer = ''
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            formatted_integer = ',' + formatted_integer
        formatted_integer = digit + formatted_integer
    
    # Combine with decimal part
    if decimal_part:
        return formatted_integer + '.' + decimal_part
    else:
        return formatted_integer

@register.filter
def money_format(value):
    """
    Formats money with comma every 3 digits and 2 decimal places.
    For example: 1234567.89 becomes $1,234,567.89
    """
    if value is None:
        return '$0.00'
    
    # Format to 2 decimal places first
    formatted_value = floatformat(value, 2)
    
    # Apply custom comma formatting
    return '$' + intcomma_every_three(formatted_value) 