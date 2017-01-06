from django.conf.urls import patterns, include, url
from django.contrib import admin

#import to server media files
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

# Examples:
    # url(r'^$', 'simplemooc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns = patterns('',    
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)