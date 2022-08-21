from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter(name='admin_checked')
def admin_checked(user):
    if has_group(user, 'Admin'):
        return "checked"

@register.filter(name='member_checked')
def member_checked(user):
    if has_group(user, 'Member'):
        return "checked"
