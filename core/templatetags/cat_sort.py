from django import template
from core.models import Category
register = template.Library()

@register.inclusion_tag('cat-sort.html', takes_context=True)
def cat_sort(context):
    categories = Category.objects.filter()
    
    return {
        'categories': categories,
    }



