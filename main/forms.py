from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-contol', 'placeholder': 'Заголовок поста'}),
			'content': forms.Textarea(attrs={'class': 'form-contol', 'placehoder': 'текст поста', 'rows': 5}),
		}
