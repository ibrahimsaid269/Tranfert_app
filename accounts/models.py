# accounts/models.py

from django.db import models
from django.contrib.auth.models import User
from agencies.models import Agency


class Agent(models.Model):

    ROLE_CHOICES = [
        ('agent', 'Agent'),
        ('supervisor', 'Superviseur'),
        ('manager', 'Manager'),
    ]

    user        = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    agency      = models.ForeignKey(Agency, on_delete=models.PROTECT, verbose_name="Agence")
    role        = models.CharField(max_length=20, choices=ROLE_CHOICES, default='agent', verbose_name="Rôle")
    phone       = models.CharField(max_length=20, verbose_name="Téléphone", blank=True)
    is_active   = models.BooleanField(default=True, verbose_name="Actif")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
        ordering = ['user__last_name']

    def __str__(self):
        return f"{self.user.get_full_name()} — {self.agency.name}"

    def get_full_name(self):
        return self.user.get_full_name()