from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gralab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'homepage.views.home', name='home'),
	url(r'^gra/', include('game.urls')),
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)