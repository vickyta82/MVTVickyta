from turtle import title
from unicodedata import name
from django.shortcuts import render 
from Family.models import Member


def home_page(request):
    list_of_members = Member.objects.all()
    return render(request, "Family/Members.html", {"title": "Home Page", "list_of_members": list_of_members})

def Search (request):
    member_search = request.GET.get("member_name")
    if member_search:
        person = Member.objects.filter(member_found__icontains = name)
    else:
        person = None
    return render(request, "Family/find.html", {"member_found": person})
