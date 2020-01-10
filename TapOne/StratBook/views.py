from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django import template
from .forms import MapForm, StratForm
from django.urls import reverse


from .models import Map, Strategy, Nade

# Create your views here.
@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'StratBook/index.html'
    context_object_name = 'map_list'

    def get_queryset(self):
        return Map.objects.filter(active_duty=True).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['inactive_map_list'] = Map.objects.filter(active_duty=False).order_by('name')
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.view_map', raise_exception=True), name ='dispatch')
class MapDetailView(generic.DetailView):
    model = Map
    template_name = 'StratBook/map_detail.html'
    context_object_name = 'map'

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.view_strategy', raise_exception=True), name ='dispatch')
class StrategyDetailView(generic.DetailView):
    model = Strategy
    template_name = 'StratBook/strat_detail.html'
    context_object_name = 'strat'

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.add_map', raise_exception=True), name ='dispatch')
class CreateMapView(generic.FormView):
    form_class = MapForm
    template_name = 'StratBook/map_add.html'
    success_url = '/stratbook/'

    def form_valid(self, form):
        _map = form.save()
        return HttpResponseRedirect(reverse('StratBook:map', args=(_map.id,)))


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.delete_map', raise_exception=True), name ='dispatch')
class DeleteMapView(generic.DeleteView):
    model = Map
    template_name = 'StratBook/map_delete.html'
    context_object_name = 'map'
    success_url = '/stratbook/'

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.add_strategy', raise_exception=True), name ='dispatch')
class CreateStratView(generic.FormView):
    form_class = StratForm
    template_name = 'StratBook/strat_add.html'
    success_url = '/stratbook/'

    def form_valid(self, form):
        form.instance.map_name = get_object_or_404(Map, pk=self.kwargs['pk'])
        form.save()
        return HttpResponseRedirect(reverse('StratBook:map', args=(self.kwargs['pk'],)))

    def get_context_data(self, **kwargs):
        context = super(CreateStratView, self).get_context_data(**kwargs)
        context['map'] = get_object_or_404(Map, pk=self.kwargs['pk'])
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.edit_strategy', raise_exception=True), name ='dispatch')
class UpdateStrat(generic.UpdateView):
    model = Strategy
    template_name = 'StratBook/strat_edit.html'
    fields = ['name', 'map_name', 'description', 'team']

    def get_success_url(self):
        return reverse('StratBook:strat', args=([self.object.id]))


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.delete_strategy', raise_exception=True), name ='dispatch')
class DeleteStrat(generic.DeleteView):
    model = Strategy
    template_name = 'StratBook/strat_delete.html'
    context_object_name = 'strat'

    def get_success_url(self):
        return reverse('StratBook:map', args=([self.object.map_name.id]))

@method_decorator(login_required, name='dispatch')
class NadeIndexView(generic.ListView):
    model = Map
    template_name = 'StratBook/nade_index.html'
    context_object_name = 'map_list'

    def get_queryset(self):
        return Map.objects.filter(active_duty=True).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(NadeIndexView, self).get_context_data(**kwargs)
        context['inactive_map_list'] = Map.objects.filter(active_duty=False).order_by('name')
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.view_map', raise_exception=True), name ='dispatch')
class NadeMapDetailView(generic.DetailView):
    model = Map
    template_name = 'StratBook/map_detail_nade.html'
    context_object_name = 'map'

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('StratBook.view_nade', raise_exception=True), name ='dispatch')
class NadeDetailView(generic.DetailView):
    model = Nade
    template_name = 'StratBook/nade_detail.html'
    context_object_name = 'nade'


