from django.contrib import admin
from .models.post import Post
from .models.teclado import Teclado
admin.site.register(Post)
admin.site.register(Teclado)