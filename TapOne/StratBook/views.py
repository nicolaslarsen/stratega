from django.views import generic

from .models import Map

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'StratBook/index.html'
    context_object_name = 'map_list'

    def get_queryset(self):
        return Map.objects.order_by('name')

class MapDetailView(generic.DetailView):
    model = Map
    template_name = 'StratBook/map_detail.html'
    context_object_name = 'm'