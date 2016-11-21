from django.shortcuts import render
from django.http import HttpResponse

from .models import Book


def list_books(request):
    return HttpResponse(request.user.username)

