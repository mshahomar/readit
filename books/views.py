from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, View
# from django.http import HttpResponse

from .models import Book, Author
from .forms import ReviewForm


def list_books(request):
    """List the books that have reviews."""

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')
    context = {'books': books}
    return render(request, 'books/list.html', context)

    # return HttpResponse(request.user.username)


class AuthorList(View):

    def get(self, request):
        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter(
            published_books__gt=0
        )
        context = {'authors': authors}

        return render(request, "books/authors.html", context)


class BookDetail(DetailView):
    model = Book
    template_name = "books/book.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "books/author.html"


def review_books(request):
    """List all of the books taht we want to review"""
    books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
    context = {'books': books, }
    return render(request, "books/list_to_review.html", context)


def review_book(request, pk):
    """Review an individual book"""
    book = get_object_or_404 (Book, pk=pk)
    form = ReviewForm

    context = {
        'book': book,
        'form': form,
    }
    return render(request, "books/review_book.html", context)

