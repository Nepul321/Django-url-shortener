from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import (
    URL
)
import uuid

def HomeView(request):
    template = "home.html"
    context = {}
    return render(request, template, context)

def CreateURLView(request):
    links_used = []

    links = URL.objects.all()

    for i in links:
        links_used.append(i.url)

    if request.method == "POST":
        link = request.POST['link']
        if link not in links_used:
            uid = str(uuid.uuid4())[:5]
            URL.objects.create(
                url=link,
                url_id=uid
            )

            return HttpResponse("localhost:8000/" + uid)
        else:
            url = URL.objects.get(url=link)
            return HttpResponse(f"URL exists. <br/> localhost:8000/{url.url_id}. <br/> Count : {url.visits}")

def RedirectView(request, pk):
    url = URL.objects.get(url_id=pk)
    url.visits += 1
    url.save()
    return redirect(url.url)
