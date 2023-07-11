from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render

from MainApp.models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


# получение данных из бд
def get_snippets(request):
    snippets = Snippet.objects.filter(hide=False)
    for snippet in snippets:
        snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
    context = {"snippets": snippets, "hide": False}
    return render(request, "pages/view_snippets.html", context)


def get_snippets_hide(request):
    snippets = Snippet.objects.all()
    for snippet in snippets:
        snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
    context = {"snippets": snippets, "hide": True}
    return render(request, "pages/view_snippets.html", context)


@requires_csrf_token
def make_hidden_or_show(request, id):
    snippet = Snippet.objects.get(id=id)
    if snippet.hide:
        snippet.hide = False
    else:
        snippet.hide = True
    snippet.save()
    return HttpResponseRedirect("/snippets/list")


# сохранение данных в бд
@requires_csrf_token
def create_snippet(request):
    if request.method == "POST":
        snippet = Snippet()
        snippet.name = request.POST.get("name")
        snippet.lang = request.POST.get("lang")
        snippet.code = request.POST.get("code")
        snippet.save()
    return HttpResponseRedirect("/")


def get_snippet_for_update(request, id):
    snippet = Snippet.objects.get(id=id)
    snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
    context = {'snippet': snippet}
    return render(request, "pages/update_snippet.html", context)


def update_snippet(request):
    snippet = Snippet.objects.get(id=request.POST.get("id"))

    snippet.name = request.POST.get("name")
    snippet.lang = request.POST.get("lang")
    snippet.code = request.POST.get("code")
    snippet.save()
    return HttpResponseRedirect("/")


def delete_snippet(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        snippet.delete()
        return HttpResponseRedirect("/")
    except Snippet.DoesNotExist:
        return HttpResponseNotFound("<h2>snippet not found</h2>")


def get_snippet(request):
    return render(request, "pages/view_snippet.html")
