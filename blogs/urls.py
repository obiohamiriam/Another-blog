from django.urls import path
from.views import post_detail, post_list

app_name = 'blogs'

urlpatterns = [
    #post views
    path('', post_list, name='post_list'),
    path('<int:id>/<slug:post>/',  post_detail, name='post_detail'),
    path('<int:id>/<slug:post>/',  post_detail, name='post_detail'),
]