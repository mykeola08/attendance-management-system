from django.shortcuts import render
from .forms import UserRegisterForm
from .models import Attend
from django.utils import timezone
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()

    return render(request, "../templates/users/register.html", {'form': form})


def attend_view(request):
    status = None
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                attended_datetime = str(timezone.now())[:10]
                print(type(attended_datetime))
            except:
                pass

                attended_today = Attend.objects.filter(attender=request.user, datetime__startswith=attended_datetime)

                if str(attended_today)[10:] == "[]>":
                    status = 3
                else:
                    status = 2

                if status == 3:
                    attend_object = Attend(attender=request.user)
                    attend_object.save()
                    status = 1

    else:
        status = 0

    return render(request, "../templates/users/attend.html", {'status': status})
