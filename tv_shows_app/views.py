from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Show

def update(request, id):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/edit/'+id)
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the show to be updated, make the changes, and save
        show = Show.objects.get(id = id)
        show.title = request.POST['title']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Show successfully updated")
        # redirect to a success route
        return redirect('/shows')