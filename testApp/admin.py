from django.contrib import admin
from models import Motorizado, Confirmacion
from django.contrib.auth.forms import UserCreationForm

class MotorizadoAdmin(admin.ModelAdmin):
	form = UserCreationForm
	fields = ('username', 'password1', 'password2', 'nombre', 'identificador', 'tipo', 'empresa')
#end class

admin.site.register(Motorizado, MotorizadoAdmin)
admin.site.register(Confirmacion)