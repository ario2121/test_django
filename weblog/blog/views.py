from django.shortcuts import render
from .models import Question,Post

# Create your views here.
def index(request):
    return render(request,'index.html')

def boz(request):
    return render(request, 'bozpage.html')

def show_all_questions(request):
    all = Question.objects.all()
    return render(request,'show_all_questions.html',context={"all":all})

def post(request):
    posts= Post.objects.all()
    return render(request,'post_page.html',context={'posts':posts})