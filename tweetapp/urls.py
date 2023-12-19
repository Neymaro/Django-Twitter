from django.urls import path
from . import views
from .views import SignUpView


app_name='tweetapp'

urlpatterns = [
    path('',views.listtweets,name='listtweets'),
    path('showmytweet/',views.showmytweet,name='showmytweet'),
    path('addtweet/',views.addtweet,name='addtweet'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('deletemytweet/<int:id>',views.deletemytweet,name='deletemytweet'),
]


