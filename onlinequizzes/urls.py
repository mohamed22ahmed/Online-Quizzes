"""onlinequizzes URL Configuration

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
from django.urls import path
from lib import views

urlpatterns = [
    path('',views.index,name='index'),

    # Admin URLs:
    path('adminLogin',views.admin_login,name='adminLogin'),
    path('adminpage',views.admin_page,name='adminPage'),
    path('addStudent',views.add_student,name='addStudent'),
    path('deleteStudent', views.delete_student, name='deleteStudent'),
    # not finished
    path('showResult', views.show_result, name='showResult'),

    path('makeQuiz', views.make_quiz, name='makeQuiz'),
    path('addQuiz', views.add_quiz, name='AddQuiz'),
    path('deleteQuiz', views.delete_quiz, name='deleteQuiz'),
    path('checkAdd', views.check_add, name='checkAdd'),
    path('checkDelete', views.check_delete, name='checkDelete'),
    path('addQuestion', views.add_question, name='addQuestion'),
    path('deleteQuestion', views.delete_question, name='deleteQuestion'),
    # not finished
    path('showQuiz', views.show_quiz, name='showQuiz'),
    path('showAllQuizzes', views.showAllQuizes, name='showAllQuizzes'),
    path('showQuizzesData', views.showQuizzesData, name='showQuizzesData'),
    path('showOneQuiz', views.showOneQuiz, name='showOneQuiz'),
    path('showQuizData', views.showQuizData, name='showQuizData'),
    path('changePassword', views.change_password, name='changePassword'),

    # User URLs:
    path('userLogin',views.user_login,name='userLogin'),
    path('userpage',views.user_page,name='userPage'),
    path('showDegrees',views.show_degrees,name='showDegrees'),
]
