from django import forms

class ChatForm(forms.Form):
    user = forms.CharField(
        label='작성자',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nickname',
                'max_length':10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder':'Chat!',
                'rows':5,
                'cols':50,
            }
        )
    )