from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from django.views import View
from allauth.account.views import LoginView,SignupView
from .forms import UserLoginForm,UserSignupForm,UserProfileForm,NewsArticleForm,NewsCommentsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfileModel,NewsArticleModel,NewsCommentsModel
from django.db.models import Q



class Search(View):
    template_name = "html/index.html"

    def get(self,request,*args,**kwargs):
        category = self.kwargs.get("category")
        news = NewsArticleModel.objects.filter(category=category)
        profile=get_profile(request.user)
        context = {"news":news,"profile":profile}
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        category = request.POST.get("category", "").strip()
        if category:
            news = NewsArticleModel.objects.filter(
                Q(title__icontains=category) | 
                Q(body__icontains=category) | 
                Q(date_written__icontains=category)  |
                Q(category__icontains=category)  
            )
        else:
            news = NewsArticleModel.objects.all()  

        profile = get_profile(request.user)
        context = {"news": news, "profile": profile, "category": category}
        return render(request, self.template_name, context)

def get_profile(user):

    try:
        profile = UserProfileModel.objects.filter(user=user).first()
    except:
        profile = None
    return profile

class UserProfileUpdateView(LoginRequiredMixin, View):
    template_name = "html/profile.html"

    def get(self, request):
        user = request.user
        profile, _ = UserProfileModel.objects.get_or_create(user=user)
        return render(request, self.template_name,{"profile":get_profile(request.user)})

    def post(self, request):
        user = request.user
        profile, _ = UserProfileModel.objects.get_or_create(user=user)
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            if request.FILES.get('image'):
                if profile.image:
                    profile.image.delete(save=False) 

                profile.image = form.cleaned_data['image']
            else:
                if user.socialaccount_set.exists():
                    social_account = user.socialaccount_set.first()
                    profile.image = social_account.extra_data.get('picture')  

            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)  
            user.email = request.POST.get('email', user.email)
            user.save()

            # Save the profile
            profile.save()

            return redirect(reverse_lazy("home"))  

        return render(request, self.template_name,{"profile":get_profile(request.user)})


class UserLoginView(LoginView):
    form_class = UserLoginForm 

class UserSignupView(SignupView):
    form_class = UserSignupForm 


class HomeView(View):
    template_name = "html/index.html"
    
    def get(self,request):
        news = NewsArticleModel.objects.all()
        profile=get_profile(request.user)
        context = {"news":news,"profile":profile}
        return render(request,self.template_name,context)
    

class NewsArticleView(LoginRequiredMixin,View):
    template_name = "html/writenews.html"
    
    def get(self, request):
        profile = get_profile(request.user)  
        return render(request, self.template_name, {"profile": profile})
    
    def post(self, request):
        form = NewsArticleForm(request.POST, request.FILES)
        profile = get_profile(request.user)
        
        if form.is_valid():
            news_article = form.save(commit=False)
            news_article.author = request.user  
            news_article.save()
            return redirect(reverse_lazy("home"))  

        return render(request, self.template_name, {"form": form, "profile": profile})

class ReadArticleView(LoginRequiredMixin,View):
    template_name = "html/detail.html"
    
    def get(self,request,**kwargs):
        pk = self.kwargs.get("pk")
        news = NewsArticleModel.objects.get(id=pk)
        comments = NewsCommentsModel.objects.filter(news=news)
        no_of_comments = NewsCommentsModel.objects.filter(news=news).count()

        profile=get_profile(request.user)
        context = {"news":news,"profile":profile,"comments":comments,"no_of_comments":no_of_comments}
        return render(request,self.template_name,context)

    def post(self,request,**kwargs):
        pk = self.kwargs.get("pk")
        get_userprofile,create_userprofile = UserProfileModel.objects.get_or_create(user=request.user)
        form = NewsCommentsForm(request.POST)
        news = NewsArticleModel.objects.get(id=pk)
        comments = NewsCommentsModel.objects.filter(news=news)
        no_of_comments = NewsCommentsModel.objects.filter(news=news).count()
        profile=get_profile(request.user)
        context = {"news":news,"profile":profile,"comments":comments,"no_of_comments":no_of_comments}

        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentor = get_userprofile
            comment.news = get_object_or_404(NewsArticleModel,id=pk)
            comment.save()
            return redirect(reverse("readnews",kwargs={"pk":pk}))
         
        return render(request,self.template_name,context)