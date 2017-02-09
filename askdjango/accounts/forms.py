from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Email', help_text='로그인 아이디로 사용할 이메일을 입력해주세요.',
            validators=[EmailValidator()])

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

