from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.template import Context, loader
from game.models import Game, Genre
from django.shortcuts import render_to_response, get_object_or_404, render, HttpResponseRedirect

mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-']
	
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone', 'Android' ]


def mobileBrowser(request):
	mobile_browser = False
	ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
	if (ua in mobile_uas):
		mobile_browser = True
	else:
		for hint in mobile_ua_hints:
			if request.META['HTTP_USER_AGENT'].find(hint) > 0:
				mobile_browser = True
	return mobile_browser
	
	
def game(request, slug):
	if mobileBrowser(request):
		template = 'gra/game.html'
	else:
		template = 'gra/game.html'
	game = get_object_or_404(Game, slug=slug)
	return render_to_response(template, {"game":game})
	
	
def index(request):
	if mobileBrowser(request):
		template = 'gra/index.html'
	else:
		template = 'gra/index.html'
	list = Game.objects.filter(status=True).order_by('-publish_date')
	genre = Genre.objects.all()
	paginator = Paginator(list, 3)
	page = request.GET.get('page')
	myName = request.user
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	except(InvalidPage, EmptyPage):
		results = paginator.page(paginator.num_pages)
	response = render_to_response(template, {"results":results, "genre":genre, "user":myName})
	return response