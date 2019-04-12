from django.contrib import admin

from .models import Sala
from .models import Materie
from .models import Profesor
from .models import Rand

admin.site.register(Sala)
admin.site.register(Profesor)
admin.site.register(Materie)
admin.site.register(Rand)