from django.contrib import admin
from .models import Choice, Question, Comment

# Seçenekleri soru sayfasında tablo gibi (yan yana) gösterir
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Formun (Düzenleme ekranı) iç yapısı
    fieldsets = [
        # Yeni alanlar (author ve image) buraya eklendi
        (None,               {"fields": ["question_text", "author", "image"]}),
        ("Tarih Bilgisi",    {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    
    # Soru detay sayfasında seçenekleri gösterir
    inlines = [ChoiceInline]
    
    # Soruların listelendiği ana ekrandaki sütunlar
    # 'author' sütunu eklendi, böylece kimin yazdığını listede görebilirsin.
    list_display = ["question_text", "pub_date", "was_published_recently", "author"]
    
    # Sağ tarafa filtreleme seçenekleri ekler (Yazar ve tarihe göre)
    list_filter = ["pub_date", "author"]
    
    # Arama kutusu
    search_fields = ["question_text"]

# Modelleri kaydediyoruz
admin.site.register(Question, QuestionAdmin)

# Yeni eklediğimiz Comment (Yorum) modelini de admin panelinde görmek için kaydediyoruz
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "question", "created_at")
    list_filter = ("created_at", "author")
    search_fields = ("content", "author__username")