from supra import views as supra
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
import models


class Login(supra.SupraSession):
	#body = True

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		obj = super(Login, self).dispatch(request, *args, **kwargs)
		if request.user.is_authenticated():
			return HttpResponse('{ "nombre": "%s", "identificador": "%s","tipo": %d, "empresa": %d}' % (request.user.motorizado.nombre, request.user.motorizado.identificador, request.user.motorizado.tipo,request.user.motorizado.empresa), content_type="application/json")
		#end if
		return obj
	#end def
#end class

def is_logged(request):
	user = request.user
	if user.is_authenticated():
		return HttpResponse('{ "nombre": "%s", "identificador": "%s","tipo": %d, "empresa": %d}' % (user.motorizado.nombre, user.motorizado.identificador, user.motorizado.tipo, user.motorizado.empresa), content_type="application/json")
	#end if
	raise Http404
#end def

@csrf_exempt
def auto_asignar(request):
	identificador = request.POST.get('identificador', False)
	return HttpResponse(identificador)
#end def


class ConfirmacionView(supra.SupraFormView):
	
	model = models.Confirmacion

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ConfirmacionView, self).dispatch(request, *args, **kwargs)
	#end def
#end class