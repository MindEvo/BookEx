from django.db.models import Avg
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from .models import MainMenu
from .forms import BookForm
from .forms import CommentForm
from .forms import RatingForm

from django.http import HttpResponseRedirect

from .models import Book
from .models import Comment
from .models import Rating

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "bookMng/index.html", {'item_list': MainMenu.objects.all()})


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, "bookMng/postbook.html",
                      {'form': form, 'item_list': MainMenu.objects.all(), 'submitted': submitted})


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request, "bookMng/displaybooks.html", {'item_list': MainMenu.objects.all(), 'books': books})


@login_required(login_url=reverse_lazy('login'))
def searchresults(request):
    books = Book.objects.filter(name__icontains=request.POST.get('search'))
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request, "bookMng/searchresults.html", {'item_list': MainMenu.objects.all(), 'books': books})


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)

    ratings = Rating.objects.filter(book=Book.objects.get(id=book_id))
    avg_rating = ratings.all().aggregate(Avg('rating'))
    total = ratings.all().count()

    book.pic_path = book.picture.url[14:]

    return render(request, "bookMng/book_detail.html",
                  {'item_list': MainMenu.objects.all(), 'book': book, 'avg_rating': avg_rating, 'total': total})


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return render(request, "bookMng/book_delete.html", {'item_list': MainMenu.objects.all(), 'book': book})


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request, "bookMng/mybooks.html", {'item_list': MainMenu.objects.all(), 'books': books})


def aboutus(request):
    return render(request, "bookMng/aboutus.html", {'item_list': MainMenu.objects.all()})


@login_required(login_url=reverse_lazy('login'))
def postcomment(request, book_id):
    submitted = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                comment.name = request.user
                comment.book = Book.objects.get(id=book_id)
            except Exception:
                pass
            comment.save()
            return HttpResponseRedirect('/book_detail/' + str(book_id))
    else:
        form = CommentForm()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, "bookMng/postcomment.html",
                      {'form': form, 'item_list': MainMenu.objects.all(), 'submitted': submitted})


@login_required(login_url=reverse_lazy('login'))
def postrating(request, book_id):
    submitted = False

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            try:
                rating.name = request.user
                rating.book = Book.objects.get(id=book_id)
            except Exception:
                pass
            rating.save()
            return HttpResponseRedirect('/book_detail/' + str(book_id))
    else:
        form = RatingForm()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, "bookMng/postrating.html",
                      {'form': form, 'item_list': MainMenu.objects.all(), 'submitted': submitted})

