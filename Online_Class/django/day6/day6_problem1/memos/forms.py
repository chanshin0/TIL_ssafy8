from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    memo = forms.CharField(
        label = '메모',
        widget=forms.Textarea(
            attrs={
                'placeholder':'memo',
                'cols':50,
                'rows':5,
            }
        )
    )

    summary = forms.CharField(
        label='요약',
        widget=forms.TextInput(
            attrs={
                'maxlength':20,
                'placeholder':'summmary'
            }
        )
    )

    class Meta:
        model = Memo
        fields = '__all__'