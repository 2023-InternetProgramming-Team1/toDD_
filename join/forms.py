from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User

class SignUpForm(UserCreationForm):
    def clean_studentId(self):
        studentId = self.cleaned_data.get('studentId')
        if User.objects.filter(studentId=studentId).exists():
            raise ValidationError("이미 존재하는 학번입니다.")
        return studentId

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("비밀번호가 일치하지 않습니다.")
        return password2

    class Meta:
        model = User
        fields = ['studentId', 'first_name', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': '이름을 입력하시오.'
                }),
            'studentId': forms.TextInput(
                attrs={
                    'placeholder': '학번을 입력하시오.'
                }),
            'password1': forms.PasswordInput(
                attrs={
                    'placeholder': '비밀번호를 입력하시오.'
                }),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder': '비밀번호를 입력하시오.'
                }),
        }

class SignInForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        studentId = cleaned_data.get('studentId')
        password = cleaned_data.get('password')

        if studentId and password:
            user = User.objects.filter(studentId=studentId).first()
            if not user:
                raise ValidationError("존재하지 않는 학번입니다.")
            if not user.check_password(password):
                raise ValidationError("비밀번호가 일치하지 않습니다.")
        return cleaned_data

    class Meta:
        model = User
        fields = ['studentId', 'password']
        widgets = {
            'studentId': forms.TextInput(
                attrs={
                    'placeholder': '학번'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': '비밀번호'
                }),
        }
