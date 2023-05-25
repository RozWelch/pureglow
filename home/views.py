from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def terms(request):
    """ A view to render the terms & conditions page """

    return render(request, 'home/terms.html')
