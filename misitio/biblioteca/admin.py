from django.contrib import admin
from biblioteca.models import Editorial, Autor, Libro
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellidos', 'email')
	search_fields = ('nombre', 'apellidos')

class LibroAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'editorial', 'fecha_publicacion')
	list_filter = ('fecha_publicacion',)
	search_fields = ('titulo',)	
	date_hierarchy = 'fecha_publicacion'
	ordering = ('-fecha_publicacion',)
	fields = ('titulo', 'autores', 'editorial', 'fecha_publicacion')
	filter_horizontal = ('autores',)

admin.site.register(Editorial)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)