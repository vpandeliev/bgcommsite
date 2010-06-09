# -*- coding: iso-8859-15 -*-
from django.shortcuts import render_to_response
from django.http import *
from bgcomm.dict import *
from bgcomm.posts.models import *
from django.template import loader, RequestContext
from django.core.mail import send_mail
import datetime
#from bgcomm.models import *

def index(response):
	return render_to_response('index.html')

def langcheck(lg):
	if lg=="bg":
		return menu_bg
	elif lg=="en":
		return menu_en
	elif lg=="fr":
		return menu_fr
	else:
		return -1
		#RAISE ERROR HERE
	
def welcome(request, lg):

	post_list = Post.objects.order_by("-date")[0:5]
	
	poll_list = Poll.objects.filter(active=1).exclude(expirydate__lt=datetime.datetime.now().date()).order_by("-date")[0:1]
	event_list = Event.objects.exclude(date__lt=datetime.datetime.now().date()).order_by("date")[0:3]
#	poll_list = Poll.objects.all()
#.exclude(expirydate__lte=datetime.datetime.now().date())
	return render_to_response("home.html", {'years':a_years(), 'ads':update_ads(),'posts': post_list, 'polls': poll_list, 'events': event_list},
	context_instance = RequestContext(request, processors=[langcheck(lg)]))


def render(request, lg, page):
	return render_to_response(page + ".html", {'years':a_years(), 'ads':update_ads()},context_instance = RequestContext(request, processors=[langcheck(lg)]))
	
def render_post(request, lg, pid):
	post = Post.objects.get(id=pid)
	return render_to_response("post.html", {'years':a_years(), 'ads':update_ads(),'item':post}, context_instance = RequestContext(request, processors=[langcheck(lg)]))
	
def render_event(request, lg, pid):
	event = Event.objects.get(id=pid)
	return render_to_response("event.html", {'years':a_years(), 'ads':update_ads(),'item':event}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

def render_events(request, lg):
	event = Event.objects.all()
	return render_to_response("events.html", {'years':a_years(), 'ads':update_ads(),'events':event}, context_instance = RequestContext(request, processors=[langcheck(lg)]))


def a_years():
	archive_years = []
	a = Post.objects.order_by("date")[0:1]
	a = a[0].date.year
	b = Post.objects.order_by("-date")[0:1]
	b = b[0].date.year
	for s in range(a,b+1):
		archive_years.append(s)
	archive_years.sort()
	archive_years.reverse()
	return archive_years

def render_archive(request, lg, year):
	posts = Post.objects.filter(date__year=year).order_by("-date")
	return render_to_response("archive.html", {'year':year,'posts': posts, 'years':a_years(), 'ads':update_ads()}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

def render_thanks(request, lg):
	return render_to_response("thanks.html", {'years':a_years(), 'ads':update_ads()}, context_instance = RequestContext(request, processors=[langcheck(lg)]))
	
def update_ads():
	return Ad.objects.all().order_by("titlebg").order_by("-image")

def error_gen(lg):
	if lg=="bg":
		return ["Моля въведете тема.", "Моля въведете съобщение.", "Моля въведете валиден e-mail адрес."]
	elif lg=="en":
		return ["Enter a subject.", "Enter a message.", "Enter a valid e-mail address."]
	elif lg=="fr":
		return ["Entrez un sujet SVP.", "Entrez un message SVP.", "Entrez un courriel valide."]
	else:
		return -1
		#RAISE ERROR HERE
		
def contacttt(request, lg):
	errors = []
	error_dict = error_gen(lg)
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append(error_dict[0])
		if not request.POST.get('message', ''):
			errors.append(error_dict[1])
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append(error_dict[2])
		if not errors:
            # To be added when an e-mail server is configured: http://docs.djangoproject.com/en/dev/topics/email/
			#send_mail(
            #    request.POST['subject'],
            #    request.POST['message'],
            #    request.POST.get('email', 'noreply@example.com'),
            #    ['siteowner@example.com'],
            #)
			return HttpResponseRedirect('/'+lg+'/thanks')

	return render_to_response("contact.html", {'errors': errors,
	 		'subject': request.POST.get('subject', ''),
			        'message': request.POST.get('message', ''),
			        'emailaddr': request.POST.get('emailaddr', ''),
	'years':a_years(), 'ads':update_ads()}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

def linksbg(request, lg):
	
	r = langcheck(lg)
	if r==menu_bg:
		categories = Category.objects.filter(bg=1)
	elif r==menu_en:
		categories = Category.objects.filter(en=1)
	elif r==menu_fr:
		categories = Category.objects.filter(fr=1)
	else:
		categories = None

	return render_to_response("links.html", {'years':a_years(), 'ads':update_ads(),'cats':categories, 'lg':r}, context_instance = RequestContext(request, processors=[langcheck(lg)]))
	