from django.conf.urls.defaults import *
from django.conf import settings
from bgcomm.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	('^$', index),
	#('^$', welcome2),
	(r'^([a-z]*)$', welcome),
	(r'^(?P<lg>\w{2})/links$', linksbg),
	(r'^(?P<lg>\w{2})/posts/(?P<pid>[0-9]*)$', render_post),
	(r'^(?P<lg>\w{2})/thanks$', render_thanks),
	(r'^(?P<lg>\w{2})/contacttt$', contacttt),
	(r'^(?P<lg>\w{2})/archive/(?P<year>[0-9]*)$', render_archive),
	(r'^(?P<lg>\w{2})/events$', render_events),
	(r'^(?P<lg>\w{2})/events/(?P<pid>[0-9]*)$', render_event),
	(r'^(?P<lg>\w{2})/(?P<page>[a-z0-9]*)$', render),
	

    # Example:
    # (r'^bgcomm/', include('bgcomm.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
