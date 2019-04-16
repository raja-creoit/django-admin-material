from django.contrib import admin
from . import models


@admin.register(models.TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_1', 'text_2')
    search_fields = ('text_1', 'text_2')
    fieldsets = (
        (None, {
            'fields': (
                ('text_1', 'text_2'),
                ('choice_1'),
                'boolean_1'
            )
        }),
    )


@admin.register(models.Test2Model)
class Test2ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'test')
    raw_id_fields = ('test_2',)
    autocomplete_fields = ('test_3',)
    fieldsets = (
        (None, {
            'fields': (
                'test',
                ('test_2', 'test_3'),
            )
        }),
    )