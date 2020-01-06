from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, User


def show_articles(request):
    template = 'articles.html'

    articles = Article.objects.all()

    context = {'articles': articles}

    return render(
        request,
        template,
        context
    )


def show_article(request, id):
    template = 'article.html'

    article = get_object_or_404(Article, pk=id)

    context = {'article': article}

    return render(
        request,
        template,
        context
    )


def pay_subscription(request):
    template = 'subscribe.html'

    button = request.GET.get('buybutton')

    if button == 'paid':
        user = User.objects.get(username=request.user.username)
        user.has_subscription = True
        user.save()
        return redirect(show_articles)

    return render(
        request,
        template,
    )
