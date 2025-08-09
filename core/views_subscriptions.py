from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Topic, Subscription

@login_required
def follow_topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    Subscription.objects.get_or_create(user=request.user, topic=topic)
    return redirect("topic-detail", slug=slug)

@login_required
def unfollow_topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    Subscription.objects.filter(user=request.user, topic=topic).delete()
    return redirect("topic-detail", slug=slug)
