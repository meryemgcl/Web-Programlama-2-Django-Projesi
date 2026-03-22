import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User # Django'nun hazır kullanıcı sistemini içe aktarıyoruz

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    # 1. Özellik: Soruyu paylaşan kullanıcıyı takip etme
    # null=True ve blank=True eski soruların hata vermemesi içindir.
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Yazar")
    
    # 2. Özellik: Görsel ekleme (Pillow kütüphanesi gerektirir: pip install Pillow)
    image = models.ImageField(upload_to='poll_images/', null=True, blank=True, verbose_name="Anket Görseli")

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Yeni mi yayınlandı?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# 3. Özellik: Yorum Sistemi
# Kullanıcılar anketlerin altına düşüncelerini yazabilsin diye yeni bir tablo.
class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Yorumunuz")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.question.question_text}"