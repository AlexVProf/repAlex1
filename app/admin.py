from django.contrib import admin
from app.models import ModelAlex
import inspect
import app.models

# Register your models here.
#admin.site.register(ModelAlex)
ms = inspect.getmembers(app.models, inspect.isclass)
for model in ms: admin.site.register(model[1])