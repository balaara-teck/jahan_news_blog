

from allauth.account.forms import LoginForm,SignupForm
from django import forms
from .models import UserProfileModel ,NewsArticleModel,NewsCommentsModel

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel  
        fields = ['image']  
 
class UserSignupForm(SignupForm):
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        return user

class UserLoginForm(LoginForm):
    remember_me = forms.BooleanField(required=False, label='Remember Me')
    def login(self, *args, **kwargs):
        result = super(UserLoginForm, self).login(*args, **kwargs)
        if self.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(1209600)  
        else:
            self.request.session.set_expiry(0)
        return result
    
class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticleModel
        fields = ["title","category","related_media","body"]

class NewsCommentsForm(forms.ModelForm):
    class Meta:
        model = NewsCommentsModel
        fields = ["body"]
        

