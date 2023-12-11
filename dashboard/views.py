from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from dashboard import forms
from candidate_management import models as candidate_management_models

BASE_CONTEXT = {
    'urls': {
        'sign_up': settings.SIGN_UP_URL,
        'login': settings.LOGIN_URL,
        'logout': settings.LOGOUT_URL,
    }
}


class DashboardView(LoginRequiredMixin, View):
    """
    View to display the dashboard with candidate information.

    Methods:
    - get: Renders the dashboard page with a table of candidates.
    """
    login_url = settings.LOGIN_URL

    def get(self, request):
        """
        GET method to render the dashboard page with candidate information.
        """
        template = 'dashboard/dashboard.html'
        table_headers = [
            'Candidate ID', 'First Name', 'Last Name', 'Contact Number', 'Action'
        ]
        candidates = candidate_management_models.Candidate.objects.all()
        add_candidate_url = '/candidate/create/'
        context = {
            'table_of_candidates': {
                'table_headers': table_headers,
                'candidates': candidates,
            },
            'add_candidate_url': add_candidate_url,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)


class SignUpView(View):
    """
    View to handle user sign-up.

    Methods:
    - get: Renders the sign-up form.
    - post: Processes sign-up form data for user registration.
    """
    def get(self, request):
        template = 'dashboard/sign_up.html'
        form = forms.SignUpForm()
        context = {
            'form': form,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)
    
    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
        template = 'dashboard/sign_up.html'
        context = {
            'form': form,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)


class LoginView(View):
    """
    View to handle user login.

    Methods:
    - get: Renders the login form.
    - post: Processes login form data for user authentication.
    """
    def get(self, request):
        template = 'dashboard/login.html'
        form = forms.LoginForm()
        context = {
            'form': form,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = forms.LoginForm(request.POST)
            template = 'dashboard/login.html'
            context = {
                'form': form,
                'error': 'Please enter a correct username and password.'
            }
            context.update(BASE_CONTEXT)
            return render(request, template, context)


class LogoutView(View):
    """
    View to handle user logout.

    Methods:
    - get: Logs out the authenticated user.
    """
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect(settings.LOGIN_URL)
