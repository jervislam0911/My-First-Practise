from django.db import models
from django.utils import timezone

PRIORITY_CHOICES = (('Python', 'Python'),
                    ('Django', 'Django'),
                    ('GitHub', 'GitHub'))


# class Article(models.Model):
#     post = models.ForeignKey("blog.Post", related_name='articles')
#     text = models.TextField()
#     code = models.TextField(max_length=600, null=True, blank=True)
#     create_date = models.DateTimeField(default=timezone.now)
#     publish_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.publish_date = timezone.now()
#         self.save()
#
#     def approved_comments(self):
#         return self.comments.filter(approved_comment=True)
#
#
# class Image(models.Model):
#     post = models.ForeignKey("blog.Post", related_name='images')
#     picture = models.ImageField(upload_to='../photos', default='pic')


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default='Python')
    text = models.TextField()
    code = models.TextField(max_length=600, null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='../photos', default='pic')
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # related_name for accessing comment from post model
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

