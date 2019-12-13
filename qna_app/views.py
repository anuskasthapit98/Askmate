from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import QuestionModel, CategoryModel,AnswerModel
from django.http import HttpResponse
from django.views.generic import CreateView, ListView



# Create your views here.
def addquestion(request):

    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('failed')
        else:            
            return HttpResponse(form.errors)
    
    else:
        form = QuestionForm
        category = CategoryModel.objects.all()
        # return render( request,"question.html", {"question":question})
        return render( request,"questionmodel_create.html", {"category":category})


def update_question(request,id):
    question = QuestionModel.objects.get(id=id)
    if request.method == "POST":
       
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid:
            try:

                form.save()
                return redirect('qna:update',id)
            except:
                return HttpResponse('failed')
        else:            
            return HttpResponse(form.errors)
    
    else:

        form = QuestionForm(instance=question)
        # return render( request,"question.html", {"question":question})
        return render( request,"questionmodel_update.html", {"form":form})


def delete_question(request,id):
    
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')

def up_vote(request,id):

    instance=QuestionModel.objects.get(id=id)
    instance.question_votes +=1
    instance.save()
    return redirect('qna:read')

def question_detail(request,id):
    questions=QuestionModel.objects.get(id=id)
    answers= AnswerModel.objects.filter(question=id)
    d={
        'question':questions,
        'answers':answers
    }

    return render(request,'details.html',d)


def questionlist(request):
    lists = QuestionModel.objects.all()
    return render (request,"questionmodel_list.html",{'question_list':lists})


class QuestionModelCreateView(CreateView):
    model = QuestionModel
    fields = '__all__'

class QuestionModelListView(ListView):
    model = QuestionModel
    queryset = QuestionModel.objects.all()