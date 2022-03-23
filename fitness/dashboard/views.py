from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import WeightForm
from django.contrib import messages
from .models import Weight
from django.shortcuts import get_object_or_404
from django.utils import timezone


class SecureView(LoginRequiredMixin, View):
    """Inherit views from this"""
    pass


class HomeView(SecureView):
    def get(self, request):
        return render(request, "dashboard/home.html")


class WeightCheckInView(SecureView):
    """Handles the Weight Creation"""

    def get(self, request):
        """New Entry for Weight for day"""
        form = WeightForm(initial={"entry_date": timezone.now().date()})
        context = {"form": form}
        return render(request, "dashboard/checkin/new.html", context)

    def post(self, request):
        """Create new Weight entry for day"""
        weight = Weight(profile=request.user.profile)
        #
        form = WeightForm(request.POST, instance=weight)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for your weight!")
            return redirect("dashboard:home")
        context = {"form": form}
        return render(request, "dashboard/checkin/new.html", context)


class WeightsView(SecureView):
    """Dashboard partial"""

    def get(self, request):
        """Display Weights in dashboard partial"""
        weights = Weight.objects.order_by("-entry_date").all()
        context = {"weights": weights}
        return render(request, "dashboard/weights/_summary.html", context)


class WeightView(SecureView):
    def get(self, request, pk):
        """Display a selected Weight"""
        weight = get_object_or_404(Weight, pk=pk)
        context = {"weight": weight}
        return render(request, "dashboard/weights/show.html", context)


class DestroyWeight(SecureView):
    def post(self, request, pk):
        """Destroy the selected Weight"""
        get_object_or_404(Weight, pk=pk).delete()    
        return redirect("dashboard:home")
