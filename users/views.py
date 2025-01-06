from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms.create import CreateUser
from users.forms.edit import EditUser
from users.models import User


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")


def list(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})


def catalog(request):
    users = User.objects.all()
    return render(request, "catalog.html", {"users": users})


def details(request, id):
    user = User.objects.get(id=id)
    # TODO: check if user exists

    return render(request, "details.html", {"user": user, "return_url": "/"})


def create(request):

    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "create.html", {"form": form, "return_url": "/"})


def edit(request, id):

    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

    form = EditUser(instance=user)

    if request.method == "POST":
        form = CreateUser(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "edit.html", {"form": form, "return_url": "/"})


def delete(request, id):
    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

    user.delete()

    return redirect("/users")
