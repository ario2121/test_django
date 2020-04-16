from django.urls import path
from .views import index, boz, show_all_questions, post
urlpatterns = [
    path('',index, name='index'),
    path('boz/', boz, name='boz'),
    path('show_all_qustions/', show_all_questions, name='show_all_questions'),
    path('posts/',post, name='posts')
]
