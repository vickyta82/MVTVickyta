from ast import Return
from asyncore import read
from contextvars import Context
from django.http import HttpResponse
from django.template import Template, Context


def Family(request):
    return HttpResponse("Family Members are as follow:")

def Members_List(request):
    file = open(r"C:\Users\vlapa\Desktop\Python\MVTVicky\MVTVicky\MVTVicky\templates\MembersList.html")
    temp = Template(file.read())
    file.close()

    context = Context()

    document = temp.render(context)
    return HttpResponse(document)


    