from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class Map(models.Model):
    name = models.CharField(max_length=50)
    active_duty = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def ct_strategies(self):
        return self.strategy_set.order_by('name').filter(team='CT')
    def t_strategies(self):
        return self.strategy_set.order_by('name').filter(team='T')
    def smokes(self):
        return self.nade_set.filter(nade_type='S')
    def molotovs(self):
        return self.nade_set.filter(nade_type='M')
    def flashes(self):
        return self.nade_set.filter(nade_type='F')
    def HEs(self):
        return self.nade_set.filter(nade_type='H')

class Strategy(models.Model):
    TEAM_CHOICES = [
        ('T', 'Terrorist'),
        ('CT', 'Counter-Terrorist')
    ]
    map_name = models.ForeignKey(Map, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=2, choices=TEAM_CHOICES)
    added_date = models.DateTimeField('date added', default=timezone.now)

    def __str__(self):
        return self.name

def nade_directory_path(instance, filename):
    return 'nades/{0}_{1}'.format(instance.map_name.id, filename)

class Nade(models.Model):
    NADE_TYPE_CHOICES = [
        ('S', 'Smoke'),
        ('M', 'Molotov'),
        ('F', 'Flash'),
        ('H', 'HE Grenade')
    ]
    name = models.CharField(max_length=50)
    map_name = models.ForeignKey(Map, on_delete=models.SET_NULL, null=True)
    nade_type = models.CharField(max_length=1, choices=NADE_TYPE_CHOICES)
    description = models.TextField(blank=True)
    img_link = models.URLField(blank=True)
    img = models.ImageField(upload_to=nade_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_image_url(self):
        if (self.img):
            return self.img.url
        if (self.img_link):
            return self.img_link
        return '';

    def type_text(self):
        for (t, name) in self.NADE_TYPE_CHOICES:
            if self.nade_type == t:
                return name

class Bullet(models.Model):
    text = models.CharField(max_length=200)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    player = models.ForeignKey(get_user_model(),
            on_delete=models.SET_NULL, blank=True, null=True)
    nade = models.ForeignKey(Nade, on_delete=models.SET_NULL, blank=True, null=True)
