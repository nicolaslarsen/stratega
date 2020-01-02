from django.db import models
from django.utils import timezone

# Create your models here.
class Map(models.Model):
    name = models.CharField(max_length=50)
    active_duty = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_ct_strategies(self):
        return self.strategy_set.order_by('name').filter(team='CT')

    def get_t_strategies(self):
        return self.strategy_set.order_by('name').filter(team='T')

class Strategy(models.Model):
    map_name = models.ForeignKey(Map, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    team = models.CharField(max_length=2)
    added_date = models.DateTimeField('date added', default=timezone.now)

    def __str__(self):
        return self.name
