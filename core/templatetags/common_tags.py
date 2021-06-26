from django import template
from core.models import Category
register = template.Library()


@register.inclusion_tag('header.html', takes_context=True)
def show_top_menu(context):
    categories = Category.objects.filter(parent=None)
    
    return {
        'categories': categories,
    }
