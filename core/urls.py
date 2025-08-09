from django.urls import path
from .views import home, topic_detail

urlpatterns = [
    path('', home, name='home'),
    path('topic/<slug:slug>/', topic_detail, name='topic-detail'),
]
