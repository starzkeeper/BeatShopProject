from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
import re

from django.db.models import QuerySet
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from beats.validators import validate_cover
from .CHOICES_FOR_BEAT import GENRE_CHOICES, KEY_CHOICES
import os


class BeatQuerySet(models.QuerySet):  # No need
    def active_beats(self):
        return self.filter(active=True)


class BeatManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return BeatQuerySet(self.model, using=self._db)

    def active_beats(self):
        return self.get_queryset().active_beats()


class Beat(models.Model):
    name = models.CharField(max_length=21, verbose_name='name')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='author')
    file = models.FileField(upload_to='songs/', validators=[FileExtensionValidator(allowed_extensions=
                                                                                   ['mp3', 'wav'])],
                            verbose_name='audio')
    cover = models.ImageField(
        upload_to='covers/', validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_cover],
        verbose_name='cover', default=None, null=True, blank=True)

    description = models.TextField(default=None, blank=True, max_length=256, null=True, verbose_name='Описание')
    bpm = models.PositiveSmallIntegerField(default=0, verbose_name='BPM')
    key = models.CharField(choices=KEY_CHOICES, max_length=50, verbose_name='Тональность')
    tags = models.CharField(default=None, max_length=100, blank=True, null=True, verbose_name='Хэштеги')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    likes = models.ManyToManyField(get_user_model(), related_name='blog_posts', blank=True, verbose_name='Лайки')
    active = models.BooleanField(default=True, verbose_name='Инструментал на продаже')
    uploaded = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, verbose_name='Жанр')

    price = models.PositiveIntegerField(default=0, verbose_name='Цена')

    objects = models.Manager()
    active_beats = BeatManager()

    class Meta:
        ordering = ('name', )

    def save(self, *args, **kwargs):
        if self.tags:
            tags_list = [f'#{tag.strip()}' for tag in self.tags.split('#') if re.match(r'^[a-zA-Z0-9]+$', tag.strip())]
            self.tags = ' '.join(tags_list)
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} by {self.author}'


# Сигналы
@receiver(pre_save, sender=Beat)
def delete_previous_song_files(sender, instance, **kwargs):
    # Проверяем, был ли экземпляр модели уже сохранен в базе данных
    if instance.pk:
        # Получаем предыдущий экземпляр из базы данных
        old_instance = Beat.objects.get(pk=instance.pk)

        # Удаляем предыдущий файл с битом, если он изменился
        if old_instance.file != instance.file and old_instance.file:
            file_path = old_instance.file.path
            if os.path.exists(file_path):
                os.remove(file_path)

        # Удаляем предыдущий файл с обложкой, если он изменился
        if old_instance.cover != instance.cover and old_instance.cover:
            cover_path = old_instance.cover.path
            if os.path.exists(cover_path):
                os.remove(cover_path)


@receiver(post_delete, sender=Beat)
def delete_song_files(sender, instance, **kwargs):
    # Удаляем файл с битом
    if instance.file:
        file_path = instance.file.path
        if os.path.exists(file_path):
            os.remove(file_path)

    # Удаляем файл с обложкой
    if instance.cover:
        cover_path = instance.cover.path
        if os.path.exists(cover_path):
            os.remove(cover_path)
