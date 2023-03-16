from django import template
from forum.models import Category

register = template.Library()

@register.inclusion_tag('forum/categories.html')
def get_categories_list(current_category = None):
    return{'categories': Category.objects.all(),
           'current_category': current_category}