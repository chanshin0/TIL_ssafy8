from django import forms
from .models import Article

# 상속받을 땐 첫 글자가 대문자여야함.(첫 글자가 대문자라는 건 class를 의미함)
# class ArticleForm(forms.Form): 
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) 

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the title',
                'maxlength':10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the contents',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required':'Please 내용 입력'
        },
    )

    class Meta:
        model = Article    # models.py에 만든 class
        fields = '__all__' # 필'즈'!! : model에 있는 애 전부 다 쓰겠다.
        # exclude = ('title',)  # 쉼표 안찍으면 튜플이 아니라 문자열로 인식해서 오류남!!!