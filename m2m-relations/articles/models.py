from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=64, verbose_name='Тэг')
    article_scope = models.ManyToManyField(
        Article, through='Relationships', through_fields=('tags', 'articles'),related_name='scopes'
    )


class Relationships(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Основная')
