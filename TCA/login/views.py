# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


class Login(View):
    """Controller for login interface."""

    def get(self, request):
        """Show login form."""
        if request.user.is_authenticated():
            # TODO: Change to dashboards
            return redirect('/')
        return render(request, 'login/login.html')

    def post(self, request):
        """Authenticate and redirect login."""
        user = self._authenticate(request)
        is_valid = self._validate_user(request, user)
        if is_valid:
            login(request, user)
            return redirect(reverse('accounts.login'))
        response = self._return_invalid_message(request)
        return response

    def _authenticate(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        return user

    def _validate_user(self, request, user):
        if user is None:
            return self._return_invalid_message(request)
        return True

    def _return_invalid_message(self, request):
        message = 'Nombre de usuario o contraseña no válido'
        return render(request, 'login/login.html', {'message': message})


def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('/')
