# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from .models import Agent
from agencies.models import Agency


class AgentForm(forms.Form):
    # Infos utilisateur
    first_name = forms.CharField(
        max_length=100, label="Prénom",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100, label="Nom",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=100, label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=False, label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    # Infos agent
    agency = forms.ModelChoiceField(
        queryset=Agency.objects.filter(is_active=True),
        label="Agence",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    role = forms.ChoiceField(
        choices=Agent.ROLE_CHOICES, label="Rôle",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    phone = forms.CharField(
        required=False, label="Téléphone",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


@login_required
def agent_list(request):
    agents = Agent.objects.select_related('user', 'agency').all()
    return render(request, 'accounts/agent_list.html', {'agents': agents})


@login_required
def agent_create(request):
    form = AgentForm()
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            # Crée l'utilisateur Django
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data.get('email', ''),
            )
            # Crée le profil agent
            Agent.objects.create(
                user=user,
                agency=form.cleaned_data['agency'],
                role=form.cleaned_data['role'],
                phone=form.cleaned_data.get('phone', ''),
            )
            messages.success(
                request,
                f"✅ Agent {user.get_full_name()} créé avec succès !"
            )
            return redirect('agent_list')
    return render(request, 'accounts/agent_form.html', {'form': form})