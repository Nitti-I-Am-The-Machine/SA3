from django.shortcuts import render

# Create your views here.
def bibliografia (requests):
    return render(requests, "bibliografia.html", context={
        "nome" : "Arthur",
        "lista" : range(1, 7)
    })