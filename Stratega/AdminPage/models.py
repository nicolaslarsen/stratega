from django.db import models

# Create your models here.
class Admin(models.Model):
    class Meta:
        permissions = (
            ('can_swap_strats', 'Can swap the strategies between two players'),
            ('can_see_hidden_strats', 'Can see hidden strategies'),
        )
