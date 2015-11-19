# coding=utf-8
from django.shortcuts import render, redirect
from django.http import Http404
import models
import forms


def index(request):
    return redirect(welcome, permanent=True)


def welcome(request):
    return render(request, "welcome.html")


def show_list(request):
    if "filt_author" in request.GET:
        filt_author = request.GET["filt_author"]
        books = models.Book.objects.filter(AuthorID__Name__icontains=filt_author)
    else:
        filt_author = ""
        books = models.Book.objects.all()

    if "add_book" in request.POST:
        book_form = forms.BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            book_form = forms.BookForm()
    else:
        book_form = forms.BookForm()

    if "remove_book" in request.GET:
        remove_isbn = int(request.GET["remove_book"])
        try:
            models.Book.objects.get(ISBN=remove_isbn).delete()
        except models.Book.DoesNotExist:
            pass
        return redirect(show_list)
    authors = models.Author.objects.all()

    # def new_author_form():
    #     if "modify_author" in request.GET:
    #         modify_id = request.GET["modify_author"]
    #         try:
    #             return forms.AuthorForm(instance=models.Author.objects.get(AuthorID=modify_id))
    #         except models.Author.DoesNotExist:
    #             return forms.AuthorForm()
    #     return forms.AuthorForm()

    if "add_author" in request.POST:
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            author_form = forms.AuthorForm()
            # author_form = new_author_form()
    else:
        author_form = forms.AuthorForm()
        # author_form = new_author_form())

    if "remove_author" in request.GET:
        remove_id = int(request.GET["remove_author"])
        try:
            models.Author.objects.get(AuthorID=remove_id).delete()
        except models.Author.DoesNotExist:
            pass
        return redirect(show_list)
    context = {"books": books, "authors": authors, "filt_author": filt_author, "author_form": author_form,
               "book_form": book_form}

    if "commit_modify" in request.POST:
        modify_isbn = long(request.POST["commit_modify"])
        try:
            modify_obj = models.Book.objects.get(ISBN=modify_isbn)
            modify_form = forms.BookForm(request.POST, instance=modify_obj)
            if modify_form.is_valid():
                modify_form.save()
            else:
                context["modify_isbn"] = modify_isbn
                context["modify_form"] = modify_form
        except models.Book.DoesNotExist:
            pass
    elif "request_modify" in request.GET:
        modify_isbn = long(request.GET["request_modify"])
        try:
            modify_obj = models.Book.objects.get(ISBN=modify_isbn)
            context["modify_isbn"] = modify_isbn
            context["modify_form"] = forms.BookForm(instance=modify_obj)
        except models.Book.DoesNotExist:
            pass

    return render(request, "show_list.html", context)


def details(request):
    if "isbn" in request.GET:
        isbn = long(request.GET["isbn"])
        book = models.Book.objects.get(ISBN=isbn)
        return render(request, "details.html", {"book": book})
    else:
        raise Http404("必须指定图书的ISBN码。")
