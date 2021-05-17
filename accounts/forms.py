from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='имя', widget=forms.TextInput(attrs={
        'placeholder': 'введите имя'
    }))
    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={
        'placeholder': 'введите пароль'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('такого пользователя не существует')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('пароль неверный')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('данный пользователь не активен')
        return super().clean(*args, **kwargs)


class SignUpForm(forms.ModelForm):
    username = forms.CharField(label='имя', widget=forms.TextInput(attrs={
        'placeholder': 'введите имя'
    }))
    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={
        'placeholder': 'введите пароль'
    }))
    password2 = forms.CharField(label='подтвердите пароль', widget=forms.PasswordInput(attrs={
        'placeholder': 'введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('пароли не совпадают')
        else:
            return data['password2']
