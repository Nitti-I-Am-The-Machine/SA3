from django.shortcuts import render

# Create your views here.
def sobre (requests):
    return render(requests, "sobre.html", context={
        "nome" : "Arthur",
        "lista" : range(1, 7)
    })