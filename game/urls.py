from django.conf.urls import patterns, include, url
from game import views

urlpatterns = patterns('game',
	url(r'^(?P<slug>\w+)/$', 'views.game', name='game_name'),
	url(r'^$', 'views.index', name='game_index'),
)
