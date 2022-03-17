from django.urls import path
from . import views

from .views import index,about,contact,events,gallery,join_now,training,videos
urlpatterns =[
    # path('',base,name='base'),
    path('',index,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('events/',events,name='events'),
    path('gallery/',gallery,name='gallery'),
    path('join_now/',join_now,name='join_now'),
    path('training/',training,name='training'),
    path('videos/',videos,name='videos'),

    
    
    
    
]



