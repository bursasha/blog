from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Ссылка')
    body = models.TextField(blank=True, db_index=True, verbose_name='Тело поста')
    date_pubs = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name='Теги')

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название тега')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка')

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
