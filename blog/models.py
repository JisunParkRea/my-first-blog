from django.db import models
from django.conf import settings
from django.utils import timezone

# 모델(객체) 정의
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 다른 모델에 대한 링크
    title = models.CharField(max_length=200) # 글자수가 제한된 텍스트
    text = models.TextField() # 글자수에 제한이 없는 긴 텍스트
    created_date = models.DateTimeField(default=timezone.now) # 날짜와 시간
    published_date = models.DateTimeField(blank=True, null=True)

    # Post 모델의 날짜와 시간을 알려주는 메소드
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Post 모델의 제목을 알려주는 메소드
    def __str__(self):
        return self.title