from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream, Category

def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
        ).filter(
            Q(is_on_main=True)
            & Q(is_published=True)
            | Q(title__contains='пломбир')
            & Q(is_published=True))
    # categories = Category.objects.values(
    #     'id', 'title', 'output_order'
    # ).order_by(
    #         'output_order', 'title'
    # )
    context = {
        'ice_cream_list': ice_cream_list,
        # 'categories': categories
    }
    return render(request, template, context)
