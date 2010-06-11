# -*- coding: iso-8859-15 -*-
from django.db import models
from tinymce import models as tinymce_models


import datetime

class Person(models.Model):
	namebg = models.CharField('Име (кирилица)',max_length=140)
	nameen = models.CharField('Име (латиница)',max_length=140)
	posbg = models.CharField('Длъжност (BG) (optional)', max_length=140)
	posen = models.CharField('Длъжност (EN) (optional)', max_length=140, blank=True)
	posfr = models.CharField('Длъжност (FR) (optional)', max_length=140, blank=True)
	contact_email = models.EmailField('Контакт за сведение (e-mail) (optional)', blank=True)
	contact_phone = models.CharField('Контакт за сведение (phone) (optional)', blank=True, max_length=30)
	
	def __unicode__(self):
	        return u'%s - %s' % (self.namebg, self.posbg)

class Post(models.Model):
	author = models.CharField('Author', max_length=140)
	titlebg = models.CharField('Title (BG)',max_length=140)
	textbg = tinymce_models.HTMLField('Text (BG)')
	titleen = models.CharField('Title (EN)',max_length=140)
	texten = tinymce_models.HTMLField('Text (EN)')
	titlefr = models.CharField('Title (FR)',max_length=140)
	textfr = tinymce_models.HTMLField('Text (FR)')
	date = models.DateTimeField('Date and time of release')
	first_paragraph_bg = None
	first_paragraph_en = None
	first_paragraph_fr = None
	def __unicode__(self):
	        return u'%s - %s' % (self.titleen, self.date)
	
	
'''	titlebg = models.CharField('Заглавие (BG)',max_length=140)
	titleen = models.CharField('Заглавие (EN)',max_length=140)
	titlefr = models.CharField('Заглавие (FR)',max_length=140)
	author = models.CharField('Автор', max_length=140)
	textbg = models.CharField('Кратък текст (BG)', max_length=3000)
	moretextbg = models.CharField('Още текст (BG) (optional)', max_length=30000, blank=True)
	texten = models.CharField('Кратък текст (EN)', max_length=3000)
	moretexten = models.CharField('Още текст (EN) (optional)', max_length=30000, blank=True)
	textfr = models.CharField('Кратък текст (FR)', max_length=3000)
	moretextfr = models.CharField('Още текст (FR) (optional)', max_length=30000, blank=True)
	date = models.DateTimeField('Дата (използвайте Today)')'''
	


class Category(models.Model):
	titlebg = models.CharField('Категория (BG)',max_length=140, blank=True)
	titleen = models.CharField('Категория (EN)',max_length=140, blank=True)
	titlefr = models.CharField('Категория (FR)',max_length=140, blank=True)
	
	CHOICES = (
        (1, 'Достъпна'),
        (0, 'Недостъпна'),
    )
	bg = models.IntegerField("На български", max_length=1, choices=CHOICES)
	en = models.IntegerField("На английски", max_length=1, choices=CHOICES)
	fr = models.IntegerField("На френски", max_length=1, choices=CHOICES)
	def __unicode__(self):
		if self.titlebg != "":
			return u'%s' % (self.titlebg)
		elif self.titleen != "":
			return u'%s' % (self.titleen)
		elif self.titlefr != "":
			return u'%s' % (self.titlefr)
		else:
			return u'%s' % ("Please enter at least one category title!")
		

	def links(self):
		return self.link_set.all()
	
class Link(models.Model):
	titlebg = models.CharField('Текст на връзката (BG)',max_length=140, blank=True)
	titleen = models.CharField('Текст на връзката (EN)',max_length=140, blank=True)
	titlefr = models.CharField('Текст на връзката (FR)',max_length=140, blank=True)
	link = models.URLField('URL')
	category = models.ForeignKey(Category)
	
	def __unicode__(self):
		if self.titlebg != "":
			return u'%s - %s' % (self.titlebg, self.link)
		elif self.titleen != "":
			return u'%s - %s' % (self.titleen, self.link)
		elif self.titlefr != "":
			return u'%s - %s' % (self.titlefr, self.link)
		else:
			return u'%s' % ("Please enter at least one link title!")

class Poll(models.Model):
	ACTIVE_CHOICES = (
        (1, 'Активна (ще се вижда на сайта)'),
        (0, 'Неактивна (няма да се вижда)'),
    )
	name = models.CharField('Вътрешно име на анкетата', max_length=140)
	code = models.CharField('Paste-нете кода от Polldaddy.com', max_length=600)
	active = models.IntegerField(max_length=1, choices=ACTIVE_CHOICES)
	date = models.DateTimeField('Дата (използвайте Today)')
	expirydate = models.DateField('Видим до дата')
 	
	def __unicode__(self):
		if self.active==1:
			r = '  --ACTIVE'
		else:
			r = ''
		if self.expirydate < datetime.datetime.now().date():
			s = '  --EXPIRED'
		else:
			s = ''
		return u'%s - %s: %s %s' % (self.name, self.date, r, s)

class Price(models.Model):
	category = models.CharField('Category',max_length=140)
	cost = models.IntegerField('Price $')
	
	def __unicode__(self):
		"""docstring for __unicode__"""
		return u'%s - %s$' % (self.category, self.cost)
		
class Event(models.Model):
	namebg = models.CharField('Title (BG)',max_length=140)
	descriptionbg = tinymce_models.HTMLField('Text (BG)')
	nameen = models.CharField('Title (EN)',max_length=140)
	descriptionen = tinymce_models.HTMLField('Text (EN)')
	namefr = models.CharField('Title (FR)',max_length=140)
	descriptionfr = tinymce_models.HTMLField('Text (FR)')
	location = models.CharField('Aдрес (на латиница)', max_length=400)
	cost = models.CharField('Цена (на латиница)', max_length=400)
	contact_name = models.CharField('Контакт за сведение (име на латиница)', blank=True, max_length=50)
	contact_email = models.EmailField('Контакт за сведение (e-mail) (optional)', blank=True)
	contact_phone = models.CharField('Контакт за сведение (phone) (optional)', blank=True, max_length=30)
	date = models.DateTimeField('Дата и час')
	
	def __unicode__(self):
		return u'%s - %s' % (self.namebg, self.date.date())

class Ad(models.Model):
	titlebg = models.CharField('Заглавие (BG)', max_length=140)
	titleen = models.CharField('Заглавие (EN)', max_length=140)
	titlefr = models.CharField('Заглавие (FR)', max_length=140)
	location = models.CharField('Aдрес (на латиница) (optional)', max_length=400, blank=True)
	image = models.CharField('Картинка (качете в /ads/)', max_length=400, blank=True)
	descriptionbg = models.CharField('Текст (BG)', max_length=3000)
	descriptionen = models.CharField('Текст (EN)', max_length=3000)
	descriptionfr = models.CharField('Текст (FR)', max_length=3000)
	contact_name = models.CharField('Контакт за сведение (име на латиница)', blank=True, max_length=50)
	contact_email = models.EmailField('Контакт за сведение (e-mail) (optional)', blank=True)
	contact_phone = models.CharField('Контакт за сведение (phone) (optional)', blank=True, max_length=30)
	expirydate = models.DateField('Платена до дата')
	link = models.URLField('URL')
	def __unicode__(self):
		return u'%s - valid until %s' % (self.titlebg, self.expirydate)