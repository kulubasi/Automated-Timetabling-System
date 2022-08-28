from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *

# Create your views here.

def index(request):
	msg=None
	if request.method == "POST":
		form=coursesform(request.POST)
		if form.is_valid():
			user=form.save()
			msg="Class Created successfully"
			return redirect('home')
		else:
			msg="Form is not valid" 
	else:
		form=coursesform()
	return render(request,'index.html',{'form':form, 'msg':msg})


def home(request):
	msg=None
	return render(request,'home.html',{'msg':msg})


def classes(request):
	course = courses.objects.all()
	msg=None
	return render(request,'classes.html',{'msg':msg,'courses':course})


def updateview(request, id):
  mymember = courses.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def updaterecordview(request, id):
  newcoursename = request.POST['newcoursename']
  newcoursecode = request.POST['newcoursecode']
  newlecturer = request.POST['newlecturer']
  newday = request.POST['newday']
  newroomno = request.POST['newroomno']

  member = courses.objects.get(id=id)
  member.coursename = newcoursename
  member.coursecode = newcoursecode
  member.lecturer = newlecturer
  member.day = newday
  member.roomno = newroomno
  member.save()
  return HttpResponseRedirect(reverse('home'))



def deleteview(request, id):
  member = courses.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('classes'))