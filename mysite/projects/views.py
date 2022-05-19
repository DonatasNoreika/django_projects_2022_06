from django.shortcuts import render, reverse
from django.views import generic
from .models import (Project,
                     Client,
                     Employee,
                     Invoice,
                     Job)
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')


class ProjectListView(generic.ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'project'


class UserProjectListView(generic.ListView, LoginRequiredMixin):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(manager=self.request.user)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Project
    fields = ['name', 'start_date', 'end_date', 'client']
    template_name = 'project_form.html'

    def get_success_url(self):
        return reverse('user_projects')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.manager
