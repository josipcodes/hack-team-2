from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.views.generic import DetailView, CreateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
from .forms import ProfileForm, CreateOrderForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class CreateProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        if not hasattr(self.request.user, 'profile'):
            profile = form.save(commit=False)
            profile.user = self.request.user
            profile.save()
        return redirect(self.success_url)