from django.shortcuts import render
from .forms import messageform
from django.http import HttpResponse
from .models import message
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):

	thougths = message.objects.order_by('-pub_date')

	return render(request, 'contents/home.html', {'thougths': thougths})

@login_required
def myblog(request):

	thougths = message.objects.filter(user = request.user).order_by('-pub_date')

	return render(request, 'contents/home.html', {'thougths': thougths})


@login_required
def data_form(request):

	if request.method == 'POST':
		form = messageform(request.POST)

		if form.is_valid():
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			name = request.user
			time = datetime.datetime.now()
			# print(form.cleaned_data['title'])
			m = message(user = name, title = title, description = description, pub_date = time)
			m.save()
			return HttpResponseRedirect('/')

	else:
		form = messageform()

	return render(request, 'contents/form.html', {'form': form, 'edit':1})

@login_required
def delete(request, id = None):

	message1 = get_object_or_404(message, id = id)

	message1.delete()
	return HttpResponseRedirect('/')

@login_required
def edit(request, id = None):

	if request.method == 'POST':
		form = messageform(request.POST)

		if form.is_valid():
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			name = request.user
			time = datetime.datetime.now()
			# print(form.cleaned_data['title'])
			m = message(user = name, title = title, description = description, pub_date = time)
			m.save()
			return HttpResponseRedirect('/')
	else:
		message1 = get_object_or_404(message, id = id)
		title = message1.title
		description = message1.description
		message1.delete()
		form = messageform(initial={'title':title, 'description': description})
	return render(request, 'contents/form.html', {'form': form, 'edit':0})

