from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.main,name="main_page"),
    path('json/', views.QuizViewSet.as_view()),
    path('add_quiz/',views.add_quiz),
]