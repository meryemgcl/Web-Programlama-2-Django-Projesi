from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # Ana sayfa: /polls/
    path("", views.IndexView.as_view(), name="index"),
    
    # Detay sayfası: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    
    # Sonuç sayfası: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # Oy verme işlemi: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # --- YENİ EKLENEN KISIM ---
    # Yorum yapma işlemi: /polls/5/comment/
    path("<int:question_id>/comment/", views.add_comment, name="add_comment"),
]