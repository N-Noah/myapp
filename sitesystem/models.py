from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import When, Count, Case, QuerySet

# Create your models here.
class MyPost(models.Model):

    CATEGORY = (('strategy', '攻略'),
                ('cheatcode', '裏技'),
                ('rta', 'RTA'),
                ('news', 'ニュース'))
    
    title = models.CharField(
        verbose_name = 'タイトル',
        max_length=200
        )

    content = models.TextField(
        verbose_name = '本文'
        )
    
    posted_at = models.DateTimeField(
        verbose_name = '投稿日時',
        auto_now_add=True
        )
    
    category = models.CharField(
        verbose_name = 'カテゴリ',
        max_length = 50,
        choices = CATEGORY
        )
    
    views = models.PositiveIntegerField(
        default=0
        )
    
    @staticmethod
    def with_state(user_id: int) -> QuerySet:
        return MyPost.objects.annotate(
            likes_cnt=Count('likes'),
            liked_by_me=Case(
                When(id__in=Likes.objects.filter(user_id=user_id).values(), then=1),
                default=0,
                output_field=models.IntegerField(),
            )
        )
    
    def __str__(self):
        return self.title

class Likes(models.Model):
    articles = models.ForeignKey('MyPost', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user_name = models.CharField('名前', max_length=255, default='名無し')
    message = models.TextField('本文')
    target = models.ForeignKey(MyPost, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
 
    def __str__(self):
        return self.message[:20]


