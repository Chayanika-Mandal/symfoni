from django.shortcuts import render


# Create your views here.
def home_page(request):
    context_dictionary = {}
    return render(request, "music/home-page.html", context_dictionary)
