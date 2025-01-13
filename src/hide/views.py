import time
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hide/index.html')


def posts(request):

    # Get start and end points
    start = int(request.GET.get('start', 0))
    end = int(request.GET.get('end', 0))

    #Generate a list of post
    posts = []
    for i in range(start, end + 1):
        posts.append(f'Post {i}')

    # Artificially delay the response
    time.sleep(1)

    # Return the list of post
    return JsonResponse({'posts': posts})