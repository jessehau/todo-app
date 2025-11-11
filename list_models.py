import os
import django

# Aseta asetukset
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

# Käynnistä Django
django.setup()

from django.apps import apps

# Tulosta kaikki mallit
print("Projektin mallit:\n")
for model in apps.get_models():
    app_label = model._meta.app_label
    model_name = model.__name__
    print(f"{app_label}.{model_name}")
