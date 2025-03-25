from django.shortcuts import render, redirect
from .forms import QuestionForm, CommentForm
from .models import Question

# Create your views here.
def create(request):
    # 2. 빈 화면에 작성해서 submit을 눌러서(POST)
    if request.method == 'POST': # POST로 요청이 들어오면
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions:index')
            
    # 1. create를 누르면 보여주는 빈 화면(GET요청)
    # else는 if문을 통과할 수 없음
    # if문 통과 - 유효하지 않는 경우, 바로 context로 감
    # 따라서 context에 들어간 form은 if에서 정의한 form이 들어감
    else:
        form = QuestionForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'index.html', context)


def detail(request, id):
    question = Question.objects.get(id=id)
    form = CommentForm()
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'detail.html', context)

def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect('questions:index')


def update(request, id):
    question = Question.objects.get(id=id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions:detail', id=id)

    else:
        form = QuestionForm(instance=question)
    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def comment_create(request, question_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # DB에 완전히 저장하지 말고 임시 저장해줘

            question = Question.objects.get(id=question_id)
            # 빠져있는 question_id를 찾아서 question에 담기
            comment.question = question
            # 임시 저장한 comment(id값 빠져있음)의 question 칼럼에 question(question_id) 데이터 삽입
            comment.save() # 삽입한 데이터 저장
            return redirect('questions:detail', id=question_id)
    else:
        return redirect('articles:index')

