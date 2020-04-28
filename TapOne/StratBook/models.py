from django.db import models
from django.db.models import F
from django.utils import timezone
from django.utils.encoding import iri_to_uri
from django.contrib.auth import get_user_model
from itertools import chain
import re

def map_directory_path(instance, filename):
    iri = 'maps/{0}_{1}'.format(timezone.now(), filename)
    return iri_to_uri(iri)

# Create your models here.
class Map(models.Model):
    name = models.CharField(max_length=50)
    active_duty = models.BooleanField(default=True)
    img = models.ImageField(upload_to=map_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name

    def ct_strategies(self):
        return self.strategy_set.filter(team='CT').order_by(F('category__ordering').asc(nulls_last=True), 'name')
    def t_strategies(self):
        return self.strategy_set.filter(team='T').order_by(F('category__ordering').asc(nulls_last=True), 'name')
    def smokes(self):
        return self.nade_set.filter(nade_type='S').order_by('name')
    def molotovs(self):
        return self.nade_set.filter(nade_type='M').order_by('name')
    def flashes(self):
        return self.nade_set.filter(nade_type='F').order_by('name')
    def HEs(self):
        return self.nade_set.filter(nade_type='H').order_by('name')

class Category(models.Model):
    name = models.CharField(max_length=50)
    ordering = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Strategy(models.Model):
    TEAM_CHOICES = [
        ('T', 'Terrorist'),
        ('CT', 'Counter-Terrorist')
    ]
    map_name = models.ForeignKey(Map, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=2, choices=TEAM_CHOICES)
    added_date = models.DateTimeField('date added', default=timezone.now)
    updated_date = models.DateTimeField('date added', default=timezone.now)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def team_text(self):
        for (t, name) in self.TEAM_CHOICES:
            if self.team == t:
                return name

    def is_new(self):
        time_between_insertion =  timezone.now() - self.updated_date
        return time_between_insertion.days < 7

    def print_if_new(self):
        if self.is_new():
            return "new"

    def swap_bullets(self, player1, player2):
        p1_bullets = list(player1.bullet_set.filter(strategy_id=self.id))
        p2_bullets = list(player2.bullet_set.filter(strategy_id=self.id))
        for bullet in p1_bullets:
            bullet.player = player2
            bullet.save()
        for bullet in p2_bullets:
            bullet.player = player1
            bullet.save()

    def bullets(self):
        return self.bullet_set.order_by(F('player__playerordering__number').asc(nulls_last=True))

def nade_directory_path(instance, filename):
    iri = 'nades/{0}_{1}'.format(instance.map_name.id, filename)
    return iri_to_uri(iri)

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
    setup_img_link = models.URLField(blank=True)
    setup_img = models.ImageField(upload_to=nade_directory_path, blank=True, null=True)
    img_link = models.URLField(blank=True)
    img = models.ImageField(upload_to=nade_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_setup_image_url(self):
        if (self.setup_img):
            return self.setup_img.url
        if (self.setup_img_link):
            return self.setup_img_link
        return ''

    def get_image_url(self):
        if (self.img):
            return self.img.url
        if (self.img_link):
            return self.img_link
        return ''

    def type_text(self):
        for (t, name) in self.NADE_TYPE_CHOICES:
            if self.nade_type == t:
                return name

    def has_setup(self):
        if (self.setup_img):
            return True
        elif (self.setup_img_link):
            return True
        else:
            return False

class Bullet(models.Model):
    text = models.CharField(max_length=200, blank=True)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    player = models.ForeignKey(get_user_model(),
            on_delete=models.SET_NULL, blank=True, null=True)
    nade = models.ForeignKey(Nade, on_delete=models.SET_NULL, blank=True, null=True)

    def delete_if_empty(self):
        text = self.text.strip()
        if ((text == '@player' or not text)
                and not self.nade and not self.player):
            self.delete()

    def replace_player_text(self):
        if self.player:
            name = self.player.username

            return self.text.replace("@player", name)
        else:
            return self.text

class PlayerOrdering(models.Model):
    number = models.IntegerField(blank=True, null=True)
    player = models.OneToOneField(get_user_model(),
            on_delete=models.SET_NULL, blank=True, null=True)
