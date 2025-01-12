from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'scroll/index.html')

texts = [
    "Habits are the foundation of our daily lives, shaping our behaviors and ultimately determining our success. Research shows that about 40 percent of our daily actions are habits rather than deliberate decisions. These automatic behaviors, formed through repetition, become ingrained in our neural pathways, making them both powerful tools for personal development and potential obstacles when they don't serve us well.",
    "Building positive habits requires understanding the habit loop: cue, craving, response, and reward. This psychological pattern is the backbone of every habit, and recognizing these components can help us create lasting change. The key to forming new habits lies in making them obvious, attractive, easy, and satisfying. Starting small with 'atomic habits' - tiny changes that yield remarkable results over time - is often more effective than attempting dramatic transformations.",
    "Breaking bad habits is equally important as forming good ones. The process involves identifying triggers, removing environmental cues, and replacing unwanted behaviors with positive alternatives. Scientific studies suggest that while the popular belief that it takes 21 days to form a habit isn't entirely accurate, the actual time varies between 18 to 254 days, depending on the complexity of the behavior and individual circumstances. Consistency, rather than perfection, is the key to successful habit formation."
    ]

def sections(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404('Invalid section number')
