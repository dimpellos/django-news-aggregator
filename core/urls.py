from django.urls import path

from . import views, views_auth, views_subscriptions

urlpatterns = [
    path("", views.home, name="home"),
    path("topic/<slug:slug>/", views.topic_detail, name="topic-detail"),
    path("signup/", views_auth.signup, name="signup"),
]

urlpatterns += [
    path(
        "topic/<slug:slug>/follow/",
        views_subscriptions.follow_topic,
        name="follow-topic",
    ),
    path(
        "topic/<slug:slug>/unfollow/",
        views_subscriptions.unfollow_topic,
        name="unfollow-topic",
    ),
]
