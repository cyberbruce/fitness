from django.shortcuts import render, redirect
from dashboard.views import SecureView
from django.utils import timezone
from django.contrib.messages import add_message, SUCCESS

#
from . import forms



def workouts_for_me(user):
    return user.profile.workouts.order_by("-workout_datetime")


class HomeView(SecureView):
    def get(self, request):
        """render current users workouts"""
        workouts = workouts_for_me(request.user)
        chart = request.user.profile.workouts.chart_data

        #
        return render(
            request,
            "workouts/home.html",
            {
                "workouts": workouts,
                "chart": chart,
            },
        )


class CreateWorkoutView(SecureView):
    def get(self, request):
        form = forms.WorkoutForm(
            initial={"workout_datetime": timezone.now()}
        )
       
        return render(request, "workouts/new.html", {"form": form})

    def post(self, request):        
        form = forms.WorkoutForm(request.POST)
        form.instance.profile = request.user.profile
        if form.is_valid():
            form.save()
            add_message(request, SUCCESS, "Added workout successfully!")
            return redirect("workouts:home")
        return render(request, "workouts/new.html", {"form": form})


class UpdateWorkoutView(SecureView):
    def get(self, request, pk):
        workout = request.user.profile.workouts.get(pk=pk)
        form = forms.WorkoutForm(instance=workout)
        return render(request, "workouts/edit.html", {"form": form, "workout": workout})

    def post(self, request, pk):
        workout = request.user.profile.workouts.get(pk=pk)
        form = forms.WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            add_message(request, SUCCESS, "Updated workout successfully!")
            return redirect("workouts:home")
        return render(request, "workouts/edit.html", {"form": form})


class DeleteWorkoutView(SecureView):
    def get(self, request, pk):
        workout = request.user.profile.workouts.get(pk=pk)
        return render(request, "workouts/delete.html", {"workout": workout})

    def post(self, request, pk):
        request.user.profile.workouts.get(pk=pk).delete()
        return redirect("workouts:home")
