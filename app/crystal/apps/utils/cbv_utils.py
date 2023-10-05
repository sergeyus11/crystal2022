# -*- coding: utf-8 -*-
from functools import wraps
from django.utils.decorators import available_attrs


class DecoratorChainingMixin(object):
    def dispatch(self, *args, **kwargs):
        base = super(DecoratorChainingMixin, self).dispatch
        for decorator in getattr(self, 'decorators', []):
            base = decorator(base)
        return base(*args, **kwargs)


def user_passes_test(test_func):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            raise Http404
        return _wrapped_view
    return decorator


def is_authenticated(user):
    if not user.is_authenticated:
        return False
    if not user.is_active:
        return False
    return True
