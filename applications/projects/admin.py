from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(projects)
admin.site.register(dependency)
admin.site.register(rewards)
admin.site.register(languages)
admin.site.register(framework)
admin.site.register(hardware)