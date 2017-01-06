from django.conf.urls import patterns, include, url


urlpatterns = patterns('simplemooc.core.views',    
    url(r'^$', 'home_method', name='home'),
    url(r'^contato/$', 'contact_method', name='contact'),
)