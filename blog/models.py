from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.blog.title}'


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def blog_count(self):
        return Blog.objects.filter(author=self.user).count()

    def __str__(self):
        return self.user.username
