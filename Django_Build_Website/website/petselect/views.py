from django.shortcuts import render, get_list_or_404
from .models import Pet

# Create your views here.


def index(request):
    return render(request, 'petselect/index.html')


def resp(request):
    pet_objects = get_list_or_404(
        Pet, size=request.POST['size'], hair=request.POST['length'])

    ctx = {
        'pets': pet_objects
    }
    return render(request, 'petselect/resp.html', ctx)
