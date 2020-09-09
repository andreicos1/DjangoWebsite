from topics.models import Topic

def display_topics(request):
    topics = Topic.objects.all()
    return {'topics':topics}
