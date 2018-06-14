from django.db import models


# Create your models here.
class Comment(models.Model):
    """评论类"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        """返回类的字符串表示"""
        return self.text[:20]
