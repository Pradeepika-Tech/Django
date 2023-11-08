from django.http import HttpResponse

# Create your views here.
def first_proverb_view(request):
    return HttpResponse("I am the creator of my own destiny")
