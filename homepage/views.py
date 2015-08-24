from django.template import Context, loader
from game.models import Game
from django.shortcuts import render_to_response

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
	
def home(request):
	if mobileBrowser(request):
		template = 'homepage/index.html'
	else:
		template = 'homepage/index.html'
		
	game_list = Game.objects.filter(status=True).order_by('-publish_date')[:12]
	special_list = Game.objects.filter(status=True, is_special=True).order_by('-publish_date')[:3]
	myName = request.user
	
	response = render_to_response(template, {"game_list":game_list, "user":myName, "special_list":special_list})
	return response