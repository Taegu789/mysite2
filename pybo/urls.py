from django.urls import path

from . import views
# 여기서 .의 의미는?
app_name = 'pybo'
#네임스페이스.-> 해주고 html에 네잇므페이스 pybo를 적어줘야함
urlpatterns = [
    path('',views.index, name='index'),
    # views.py의 index를 index로 호출가능하게 해버림
    path('<int:question_id>/', views.detail,name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

    # views.py의 detail을 detail이라는 것만으로 호출가능하게 바꿈.
    #매핑을 추가해서 id를 잘 잡아서 띄워줄 ㄹ것이다! by views.detail(views.py에 detail 만들어줘야댐)
]
