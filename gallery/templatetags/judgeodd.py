from django.template import Library

register = Library()


@register.filter(name="judge_odd")
def Odd(x):
    """judge odd"""
    if not isinstance(x, int):
        return True
    if x % 2 == 0:
        return False
    else:
        return True
