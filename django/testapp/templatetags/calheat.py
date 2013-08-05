from django import template
from splunkdj.templatetags.tagutils import component_context
register = template.Library()
@register.inclusion_tag('splunkdj:components/component.html', takes_context=True)
def calheat(context, id, *args, **kwargs):       # The template tag
    return component_context(
        context,
        "calheat",                           # The custom view's CSS class name
        id,
        "view",
        "testapp/calheat",             # Path to the JavaScript class/file for the view
        kwargs
    )


