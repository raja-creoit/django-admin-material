from django.contrib import admin
from . import models


@admin.register(models.TestModel)
class TestModelAdmin(admin.ModelAdmin):
    pass
