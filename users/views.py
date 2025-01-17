from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib import messages

from users.forms.create import CreateUser
from users.forms.edit import EditUser
from users.models import User

def index(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})


def catalog(request):
    users = User.objects.all()
    return render(request, "catalog.html", {"users": users})


def details(request, id):
    user = User.objects.get(id=id)
    # TODO: check if user exists

    return render(request, "details.html", {
        "user": {
            **model_to_dict(user),
            "roleName": User.ROLE_CHOICES[user.role][1]
        }, 
        "return_url": "/"})


def create(request):

    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, "User created successfully!")
            return redirect("/")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "create.html", {"form": form, "return_url": "/", "roles": User.ROLE_CHOICES})


def edit(request, id):

    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

    form = EditUser(instance=user)

    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES, instance=user)

        if request.FILES and user.avatar: # do work when avatar != None, 0, False, "", [], (), {}
            user.avatar.delete()

        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "edit.html", {"form": form, "return_url": "/"})


def delete(request, id):
    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

    if user.avatar: # do work when avatar != None, 0, False, "", [], (), {}
        user.avatar.delete()
        
    user.delete()

    return redirect("/")


class CustomLoginView(LoginView):
    # template_name = 'login.html'
    # authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # Add your authentication logic here
        return super().form_valid(form)