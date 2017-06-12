# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from weatherApp.forms import RegistrationForm
from weatherApp.tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.core.mail import send_mail
from weatherApp.models import MyUser
from django.contrib.auth import login
from django.core.urlresolvers import reverse

from rest_framework import generics
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime



def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            print user.email
            print str(user.email)
            send_mail(subject, message, 'popoolaebenezer@gmail.com', [str(user.email),], fail_silently=False)
            return redirect('weatherapp:account_activation_sent')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/account_activation_invalid.html')

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


@login_required(login_url='/weatherapp/login/')
def home(request):
    obj = Weather.objects.filter(date__gte=datetime.now())

    page = request.GET.get('page', 1)

    paginator = Paginator(obj, 3)
    try:
        weather = paginator.page(page)
    except PageNotAnInteger:
        weather = paginator.page(1)
    except EmptyPage:
        weather = paginator.page(paginator.num_pages)

    return render(request, 'weatherApp/home.html', {'weather': weather})


class CreateView(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    """This class defines the create behavior of our rest api."""
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
