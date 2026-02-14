from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-created_at"]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته  بندی"
        verbose_name_plural = "دسته  بندی ها"


class Post(models.Model):
    STATUS_CHOICES = (("draft", "پیش نویس"), ("published", "منترشده"))
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name="محتوا")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="دسته بندی",
    )

    author = models.CharField(max_length=100, verbose_name="نویسنده")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def publish(self):
        self.status = "published"
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
