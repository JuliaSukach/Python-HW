"""That module need for additional functions"""
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_user(request):
    """
    Returns user or None
    :param request: Object request
    """
    from .models import User

    pk = request.COOKIES.get('username')

    if pk:
        try:
            user = User.objects.get(pk=int(pk))
        except User.DoesNotExist:
            return None
        return user


def paginate(
        obj: object,
        size: int,
        request: object,
        context: dict,
        var_name: str = 'object_list'
) -> dict:
    """Paginate objects provided by View"""
    paginator = Paginator(obj, size)
    page = request.GET.get('page', '1')

    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)

    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context
