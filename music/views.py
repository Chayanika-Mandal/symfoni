import sys

from django.shortcuts import render


# Create your views here.
def home_page(request):
    context_dictionary = {
        "path": sys.path,
        "my_list": "wdavfsv",
        "name": "Diptesh",
    }
    return render(request, "music/home-page.html", context_dictionary)
