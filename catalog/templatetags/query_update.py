from django import template
register = template.Library()

@register.simple_tag
def query_update(query, key, value):
    query = query.copy()
    query[key] = value
    return query.urlencode()