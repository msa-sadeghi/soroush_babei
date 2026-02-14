from django.shortcuts import render, get_object_or_404
from .models import Article, Post, Category


def article_list(request):
    articles = Article.objects.filter(published=True)
    return render(request, "blog/list.html", {"articles": articles})


def home(request):
    recent_posts = Post.objects.filter(status="published")[:5]
    categories = Category.objects.all()
    context = {
        "recent_posts": recent_posts,
        "categories": categories,
        "page_title": "صفحه اصلی",
    }

    return render(request, "blog/home.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status="published")
    post.views += 1
    post.save(update_fields=["views"])

    related_posts = Post.objects.filter(
        category=post.category, status="published"
    ).exclude(id=post.id)[:3]
    context = {"post": post, "related_posts": related_posts, "page_title": post.title}
    return render(request, "blog/post_detail.html", context)
