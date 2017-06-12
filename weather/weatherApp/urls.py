from django.contrib.auth import views as auth_views
from weatherApp.views import registration, activate, account_activation_sent, home
from django.conf.urls import url, include
from django.core.urlresolvers import reverse

from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, RecordsView



urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^register/$', registration, name='registration',),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),

    url(r'^login/$', auth_views.login, {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/weatherapp/login/'}, name='logout'),

    url(r'^api/retrieve/$', RecordsView.as_view(), name="retrieve"),
    url(r'^api/create/$', CreateView.as_view(), name="create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


