
from django.conf import settings
from django.db import models
from django.utils import timezone
#models.CharField — так мы определяем текстовое поле с ограничением на количество символов.
#models.TextField — так определяется поле для неограниченно длинного текста. Выглядит подходящим для содержимого поста, верно?
#models.DateTimeField — дата и время.
#models.ForeignKey — ссылка на другую модель.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title