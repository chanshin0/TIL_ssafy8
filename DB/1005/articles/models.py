from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title

# 스키마를 만드는 부분
# CREATE TABLE
class Comment(models.Model):
    # ADD COLUMN
    # 왜래 키의 필드를 작성하는 부분
    # 왜래 키 필드는 작성 위치나 순서와 관계없이 맨 마지막 필드에 작성됨(맨 오른쪽)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

