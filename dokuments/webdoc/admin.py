from django.contrib import admin

from . import models as my_models

# Register your models here.

# classes = [getattr(my_models, name) for name in dir(my_models) if isinstance(getattr(my_models, name), type)]
#
# for cls in classes:
#     admin.site.register(cls)


def register_class(cls):
    admin.site.register(cls)

register_class(my_models.User)
register_class(my_models.Document)
register_class(my_models.Address)
register_class(my_models.Page)
register_class(my_models.Comment)
register_class(my_models.Payment)
