"""
Models for backend app.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
import uuid

class Drone(models.Model):
    """ Drone model representation"""
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    battery_capacity = models.IntegerField(default=100)
    battery_remaining = models.IntegerField(default=100)
    capabilities = models.JSONField(default=dict, blank=True,null=True)
    upgrade_slots = models.IntegerField()
    team_id = models.IntegerField()

    def __str__(self):
        return self.name
     
 
class DroneTeam(models.Model):
    """ DroneTeam model representation"""
    name = models.CharField(max_length=255)
    drones = ArrayField(
        models.IntegerField(),
        blank=True,
        null=True
    )
    player_id = models.IntegerField()
    
    def __str__(self):
        return self.name
        
class Contract(models.Model):
    """ Contract model representation"""
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    )

    name = models.CharField(max_length=255, default="none")
    description = models.CharField(max_length=255,default="none")
    requirements = models.JSONField(default=dict, blank=True,null=True)
    status = models.CharField(max_length=20,default='active', choices=STATUS_CHOICES)
    npc_id = models.IntegerField()
    player_id = models.IntegerField()
    
    drone_team_ids = ArrayField(
        models.IntegerField(),
        blank=True,
        null=True
    )

    def __str__(self):
        return  str(self.name)


class TulipField(models.Model):
    """ TulipField model representation"""
    size = models.FloatField()
    soil_type = models.CharField(max_length=50)
    contract_id = models.IntegerField()
    drone_team_id = models.IntegerField()

    def __str__(self):
        return str(self.contract_id)
    
class TulipPlant(models.Model):
    """ TulipPlant model representation"""
    tulip_type = models.CharField(max_length=50)
    growth_stage = models.IntegerField()
    health = models.FloatField()
    field_id = models.IntegerField()

    def __str__(self):
        return str(self.tulip_type)
    
class Player(models.Model):
    """Player model representation"""
    username = models.CharField(max_length=50)
    credits = models.IntegerField()
    reputation = models.JSONField(default=dict, blank=True,null=True)

    def __str__(self):
        return self.username