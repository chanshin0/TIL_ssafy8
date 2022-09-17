from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'maxlegth' : 50,
                'placeholder':'ex) 세 얼간이'
            }
        )
    )
    director = forms.CharField(
        label='감독',
        widget=forms.TextInput(
            attrs={
                'maxlegth' : 10,
                'placeholder':'ex) 라지쿠마르 히라니'
            }
        )
    )
    comment = forms.CharField(
        label='관람평',
        widget=forms.Textarea(
            attrs={
            'placeholder':'ex) 나 세 얼간이 아니다!',
            'cols':40,
            'rows':3
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ('title',)