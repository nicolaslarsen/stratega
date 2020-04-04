from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User, Group
from StratBook.models import PlayerOrdering, Map, Category
from StratBook.forms import CategoryForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django import template
from django.urls import reverse
from django.db.models import F

# Create your views here.
@method_decorator(permission_required('AdminPage.view_admin', raise_exception=True), name='dispatch')
@method_decorator(permission_required('StratBook.view_category', raise_exception=True), name='dispatch')
@method_decorator(permission_required('StratBook.view_playerordering', raise_exception=True), name='dispatch')
@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'AdminPage/index.html'
    context_object_name = 'players'

    def get_queryset(self):
        return User.objects.all().order_by(
                F('playerordering__number').asc(nulls_last=True))

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['maps'] = Map.objects.all().order_by('name')
        context['categories'] = Category.objects.all().order_by('ordering')
        return context

@permission_required('AdminPage.change_admin', raise_exception=True)
@login_required
def UpdateUser(request, pk):
    usr = User.objects.get(pk=pk)
    admin_group = Group.objects.get(name='Admin')
    member_group = Group.objects.get(name='Member')
    if request.POST['ordering'] == '':
        ordering = None
    else:
        ordering = request.POST['ordering']

    try:
        usr.playerordering.number = ordering
    except PlayerOrdering.DoesNotExist:
        PlayerOrdering(player=usr).save()
        usr.playerordering.number = ordering

    if(request.POST.get('is_member')):
        usr.groups.add(member_group)
    else:
        member_group.user_set.remove(usr)

    if(request.POST.get('is_admin')):
        usr.groups.add(admin_group)
    else:
        admin_group.user_set.remove(usr)

    usr.save()
    usr.playerordering.save()
    messages.success(request, f"User: {usr.username} was updated successfully")
    return HttpResponseRedirect(reverse('AdminPage:index'))


@permission_required('AdminPage.change_admin', raise_exception=True)
@permission_required('StratBook.change_strategy', raise_exception=True)
@login_required
def SwapStrategies(request):
    pid1 = request.POST.get('swapPlayer1','')
    pid2 = request.POST.get('swapPlayer2','')
    mapIds = request.POST.get('maps', '')
    mapStrList = []

    if (pid1 and pid2):
        player1 = User.objects.get(pk=pid1)
        player2 = User.objects.get(pk=pid2)

        if mapIds == 'all':
            maps = Map.objects.all()
        else:
            maps = Map.objects.filter(pk=mapIds)

        for _map in maps:
            mapStrList.append(_map.name)
            for strat in _map.strategy_set.all():
                strat.swap_bullets(player1, player2)
        messages.success(request, 
            f'Succesfully swapped strats between {player1} and {player2} on {mapStrList}')
    else:
        messages.error(request, 'Can not swap strategies unless two players have been selected')
    return HttpResponseRedirect(reverse('AdminPage:index'))
