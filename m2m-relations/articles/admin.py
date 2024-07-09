from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tags, Relationships


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main = 0
        for form in self.forms:
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            if cleaned_data['is_main']:
                count_main += 1
        if count_main <= 1:
            raise ValidationError('Тут всегда ошибка')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = Relationships
    extra = 1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ArticleScopeInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


