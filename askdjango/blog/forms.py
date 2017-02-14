from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'photo']

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        if len(content) % 2 == 0:
            # raise forms.ValidationError('홀수 길이로 입력하세요.')
            self.add_error('content', '홀수 길이로 입력하세요.')
        content = ' '.join(word for word in content.split())
        return content

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

