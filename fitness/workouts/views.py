from multiprocessing import get_context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.views import SecureView
from . import forms
from . import models
from django.contrib.messages import add_message, SUCCESS
from django.utils import timezone

def workouts_for_me(user):
  return user.profile.workouts.order_by('-workout_datetime')


@login_required
def home_view(request):
  """ render current users workouts """ 
  #
  return render(request, "workouts/home.html", {
    'workouts': workouts_for_me(request.user)
  })


class CreateWorkoutView(SecureView):
    def get(self, request):
        form = forms.WorkoutForm(instance=models.Workout(workout_datetime=timezone.now().date()))
        return render(request, "workouts/new.html", { 'form': form })

    def post(self, request):
        workout = models.Workout(profile=request.user.profile)
        form = forms.WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
          form.save()
          add_message(request, SUCCESS, "Added workout successfully!")
          return redirect('workouts:home')
        return render(request, "workouts/new.html", { 'form': form })

class UpdateWorkoutView(SecureView):
    def get(self, request, pk):
        workout = request.user.profile.workouts.get(pk=pk)
        form = forms.WorkoutForm(instance=workout)
        return render(request, "workouts/edit.html", { 'form': form })

    def post(self, request, pk):
        workout = request.user.profile.workouts.get(pk=pk)
        form = forms.WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
          form.save()
          add_message(request, SUCCESS, "Updated workout successfully!")
          return redirect('workouts:home')
        return render(request, "workouts/edit.html", { 'form': form })
  

class DeleteWorkoutView(SecureView):
    def get(self, request, pk):
      workout = request.user.profile.workouts.get(pk=pk)
      return render(request, "workouts/delete.html", { 'workout': workout })

    def post(self, request, pk):
        request.user.profile.workouts.get(pk=pk).delete()
        return redirect('workouts:home')