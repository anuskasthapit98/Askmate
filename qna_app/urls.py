"""askmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
app_name='qna'

urlpatterns =[
    path('addquestion/',addquestion, name='addquestion'),
    path('read/', questionlist , name='read'),
    path('update/<int:id>', update_question, name='update'),
    path('delete/<int:id>', delete_question, name='delete'),
    path('upvote/<int:id>', up_vote, name='upvote'),
    path('ques_list/', ques_list, name='test'),
    path('details/<int:id>', question_detail, name='details'),
    path('create/', QuestionModelCreateView.as_view(), name='create'),
    path('list/', QuestionModelListView.as_view(), name='list'),
    path('test/', test, name='test')
   
]
