from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required # Giriş kontrolü için

from .models import Choice, Question, Comment # Comment modelini ekledik

# 1. Ana Sayfa: Görsel ve yazar bilgisiyle birlikte listeleme yapar
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Yayınlanmış son beş soruyu getirir (gelecekte yayınlanacaklar hariç).
        select_related ve prefetch_related kullanarak veritabanı performansını artırıyoruz.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).select_related('author').order_by("-pub_date")[:5]

# 2. Detay Sayfası: Soru detayları ve yorumları gösterir
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """Henüz yayınlanmamış soruları detay sayfasında göstermez."""
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        """Şablona (HTML) ekstradan yorumları da gönderiyoruz."""
        context = super().get_context_data(**kwargs)
        # Soruya ait tüm yorumları tarihe göre sıralı çekiyoruz
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context

# 3. Sonuç Sayfası: Oylama sonuçlarını gösterir
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# 4. Oy Verme İşlemi
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Geliştirme: Sadece giriş yapmış kullanıcılar oy kullanabilsin (Güvenlik)
    if not request.user.is_authenticated:
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Oy kullanmak için giriş yapmalısınız.",
        })

    try:
        selected_choice = question.choices.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Bir seçenek belirlemediniz.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# 5. Yeni: Yorum Yapma Fonksiyonu
@login_required # Sadece giriş yapanlar yorum yapabilir
def add_comment(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                question=question,
                author=request.user,
                content=content
            )
    return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))