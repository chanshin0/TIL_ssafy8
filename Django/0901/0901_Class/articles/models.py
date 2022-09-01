from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) 
    #CharField는 게시글의 제목처럼 작은 텍스트를 저장하는 공간을 의미함 (255자)
    content = models.TextField()   # 본문의 내용을 저장할 공간. 2의 31승? 자
    created_at = models.DateTimeField(auto_now_add=True) # 최초 생성일자(a_t_n)
    updated_at = models.DateTimeField(auto_now=True)     # 최종 수정일자(a_t)

    def __str__ (self):
        return f'{self.title} / {self.content}'
