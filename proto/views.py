"""
Basic (default) views for Catalog app.
"""

from django.shortcuts import render
from catalog.models import Category, Product


def index(request):
    """
    Main page view: root categories, top products.

    :param request:
    :return: HttpResponse
    """
    root_categories = Category.objects.root_nodes()
    top_products = Product.objects.filter(is_popular=True)

    return render(
        request, 'proto/main.html', {
            'root_categories': root_categories,
            'top_products': top_products,
        })
