from django.shortcuts import render
from django.http import HttpResponse
from Dtest.models import BookInfo


# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    return render(request, 'index.html', {'content': books})
