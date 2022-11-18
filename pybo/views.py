from django.shortcuts import render
from .models import Question
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm
from .forms import AnswerForm
from django.http import HttpResponseNotAllowed
#R1위한 모듈
def index(request):
    question_list = Question.objects.order_by('-create_date')
    # 질문 목록 데이터 얻기 생성일자순으로
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    #렌더함수에서사용한 html 템플릿 파일 작성하기!
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
    # R1.id에 없는 데이터를 요청하는 경우 404 출력하기위해 약간의 수정 ㄱ
    # R1이전 : question = Question.objects.get(id=question_id)
# Create your views here.

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
        else:
            return HttpResponseNotAllowed('Only POST is possible.')
        context = {'question': question, 'form': form}
        return render(request, 'pybo/question_detail.html', context)

# 상세호출 위한 answer ceate 함수를 만들어주어서 이것을 hrl매핑 등록하서  질문상세까지연동
# 그렇게 해서 질문->바로 답변 할수있게.

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

#question_create 버튼 함수를 만들어서 버튼이 작동하도록 해주 었따.ㄴ
# 링크를통해 페이지를 요청하는 시에는 자동으로 Get.
# 그래서 위의 함수는 get/post 두가지로 작동하고. 페이지 요청시에는 get.!
# 저장하기 버튼 누르면 post!