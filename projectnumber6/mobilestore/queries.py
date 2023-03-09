from functools import reduce

from django.db.models import Q, F

from mobilestore.models import Brand, Mobile


def all_brands_not_in_korea_china():
    query = Brand.objects.filter(
        ~Q(nationality='Korea') & ~Q(nationality='China')
    )
    return query


def some_brand_mobiles(*brand_names):
    query = Mobile.objects.filter(
        reduce(lambda x, y: x | Q(brand__name=y), brand_names, Q())
    )
    return query


def mobiles_brand_nation_equals_made_in():
    query = Mobile.objects.filter(made_in=F('brand__nationality'))
    return query