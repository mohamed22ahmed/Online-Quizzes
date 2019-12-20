from django.shortcuts import render, redirect
from . import models
# Create your views here.

def index(request):
    return render(request,'lib/index.html')
'''
    start of admin Views
    
    the functions of admin are:
    1- login 
    2- add student
    3- delete  student
    4- show results for specific level
    5- set timer for quiz
    7- Make quiz:
        -> Add quiz
        -> delete quiz
        -> Add question
        -> delete question
    8- show quiz:
        -> show all for specific level
        -> show one for specific level
    9- change password for quiz
'''
def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        models.User.objects.raw('SELECT * FROM User WHERE email = email AND password=password AND status=2')
        if models.User.objects.count()>0:
            return render(request, 'lib/adminlogin.html')
        else:
            return render(request,'lib/admin.html')
    else:
        return render(request,'lib/admin.html')

def admin_page(request):
    return render(request, 'lib/adminlogin.html')

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        user_class = request.POST['user_class']
        models.User.objects.create(name=name, email =email, password=password, user_class=user_class)
        return render(request, 'lib/adminlogin.html')
    return render(request, 'lib/admin_add_student.html')

def delete_student(request):
    if request.method == 'POST':
        email = request.POST['email']
        models.User.objects.filter(email=email).delete()
        return render(request, 'lib/adminlogin.html')
    return render(request, 'lib/admin_delete_student.html')

# not finished
def show_result(request):
    if request.method == 'POST':
        user_class = request.POST['user_class']
        # return data from user_quiz table and show it in
        return render(request, 'lib/admin_show_result.html')
    return render(request, 'lib/admin_class_result.html')

def results(request):
    return render(request, 'lib/admin_show_result.html')

def make_quiz(request):
    return render(request, 'lib/admin_make_quiz.html')

def add_quiz(request):
    if request.method == 'POST':
        name = request.POST['chapter']
        quiz_class = request.POST['quiz_class']
        models.Quiz.objects.create(name=name, quiz_class=quiz_class)
        return render(request, 'lib/admin_make_quiz.html')
    return render(request, 'lib/admin_add_quiz.html')

def delete_quiz(request):
    if request.method == 'POST':
        name = request.POST['chapter']
        quiz_class = request.POST['quiz_class']
        models.Quiz.objects.filter(name = name, quiz_class = quiz_class).delete()
        return render(request, 'lib/admin_make_quiz.html')
    return render(request, 'lib/admin_delete_quiz.html')

def check_add(request):
    if request.method == 'POST':
        name = request.POST['chapter']
        quiz_class = request.POST['quiz_class']
        quiz=models.Quiz.objects.filter(name=name,quiz_class=quiz_class)
        if quiz.count() > 0:
            for e in quiz:
                request.session['quiz_id']=e.id
            return redirect('addQuestion')
    return render(request, 'lib/admin_class_quiz_add_ques.html')

def add_question(request):
    if request.method == 'POST':
        question = request.POST['question']
        choose1 = request.POST['choose1']
        choose2 = request.POST['choose2']
        choose3 = request.POST['choose3']
        choose4 = request.POST['choose4']
        correct = request.POST['correct']
        quiz_id=request.session['quiz_id']
        quiz = models.Quiz.objects.get(id=quiz_id)
        #models.Content.objects.create(question=question, choos1=choose1, choos2=choose2, choos3=choose3, choos4=choose4, correct=correct, quiz_id_id=quiz_id)
        con = models.Content(question = question,choos1=choose1, choos2=choose2, choos3=choose3, choos4=choose4, correct=correct, quiz_id=quiz)
        con.save()
        return render(request, 'lib/admin_make_quiz.html')
    return render(request, 'lib/admin_add_question.html')

def check_delete(request):
    if request.method == 'POST':
        name = request.POST['chapter']
        quiz_class = request.POST['quiz_class']
        quiz=models.Quiz.objects.filter(name=name,quiz_class=quiz_class)
        if quiz.count() > 0:
            for e in quiz:
                request.session['quiz_id']=e.id
            return redirect('deleteQuestion')
    return render(request, 'lib/admin_class_quiz_del_ques.html')

def delete_question(request):
    if request.method == 'POST':
        name = request.POST['question']
        quiz_id = request.session['quiz_id']
        quiz = models.Quiz.objects.get(id=quiz_id)
        models.Content.objects.filter(question = name, quiz_id = quiz).delete()
        return redirect('makeQuiz')
    return render(request, 'lib/admin_delete_question.html')

def showAllQuizes(request):
    if request.method == 'POST':
        quiz_class = request.POST['quiz_class']
        quiz = models.Quiz.objects.filter(quiz_class=quiz_class)
        if quiz.count() > 0:
            request.session['quizClass'] = quiz_class
            return redirect('showQuizzesData')
    return render(request, 'lib/admin_show_quizes_class.html')

def showQuizzesData(request):
    quiz_class = request.session['quizClass']
    quiz=models.Quiz.objects.raw('SELECT * FROM Quiz WHERE quiz_class = quiz_class ORDER BY name')

    # send quizzes to template
    return render(request,'lib/admin_show_quizes_all.html')

def show_quiz(request):
    return render(request, 'lib/admin_show_quizes.html')

def showOneQuiz(request):
    if request.method == 'POST':
        name = request.POST['chapter']
        quiz_class = request.POST['quiz_class']
        quiz = models.Quiz.objects.filter(name=name,quiz_class=quiz_class)
        if quiz.count() > 0:
            request.session['quizClass'] = quiz_class
            request.session['quizname'] = name
            return redirect('showQuizData')
    return render(request, 'lib/admin_show_quizes_one_quiz.html')

def showQuizData(request):
    name = request.session['quizname']
    quiz_class = request.session['quizClass']
    quiz = models.Quiz.objects.filter(name=name, quiz_class=quiz_class)
    con = models.Content.objects.filter(quiz_id=quiz)
    return render(request, 'lib/admin_show_quiz.html',{'questions':con})

def change_password(request):
    if request.method == 'POST':
        name = request.POST['chapter']
        quiz_pass = request.POST['set_pass']
        quiz_class = request.POST['quiz_class']
        models.Quiz.objects.filter(name=name,quiz_class=quiz_class).update(password=quiz_pass)
        return redirect('adminPage')
    return render(request, 'lib/admin_change_password.html')



#    End of admin views


'''
    start of student Views

    the functions of student are:
    1- login 
    2- show degrees
    3- do quiz
'''
def user_login(request):
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['pass']
        user_class = request.POST['class']
        models.User.objects.raw('SELECT * FROM User WHERE email = email AND password=password AND status=1')
        if models.User.objects.count()>0:
            request.session["user_class"]=user_class
            return render(request, 'lib/userlogin.html')
    else:
        return render(request,'lib/user.html')

def user_page(request):
    return render(request, 'lib/userlogin.html')

def show_degrees(request):
    return render(request,'lib/user_results.html')




# End of user views