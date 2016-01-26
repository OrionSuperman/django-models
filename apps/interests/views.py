from django.http import HttpResponse, Http404
from django.shortcuts import render # inserted this line
from .models import User, Interest
def index(request):
  return render(request, 'interests/index.html') # updated this line 

def interests(request):

	users = User.objects.all()

	context = {
	'users' : users,
	}
	return render(request, 'interests/interests.html', context)

def user(request, id):
	user = User.objects.get(id=id)
	context = {
	'user' : user,
	}
	return render(request, 'interests/user.html', context)