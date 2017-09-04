from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^game/', game, name='game'),
    url(r'^responses/', responses, name='responses'),
    url(r'^login/', loginpage, name='login'),
    url(r'^logout/', logoutpage, name='logout'),
]
