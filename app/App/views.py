from django.shortcuts import render,redirect
from .models import Quiz
from rest_framework import generics
from .serializers import QuizSerializer
from .forms import QuizForm
import requests,json
from django.http import JsonResponse
# Create your views here.
def main(request):
    return render(request,'main.html')


def add_quiz(request):
    if request.method == 'POST':
        userform = QuizForm(request.POST)
        if userform.is_valid():
            count = userform.cleaned_data["count"]
            if count>0:
                counter = 0
                while(count!=0):
                    url = f'https://jservice.io/api/random?count={count-counter}'
                    response = requests.get(url)
                    quizes = json.loads(response.text) 
                    for quiz in quizes:
                        try:
                            Quiz.objects.get(id = quiz['id'])
                        except:
                            counter+=1
                            new_quiz = Quiz(id = quiz['id'],text = quiz['question'],answer = quiz['answer'])
                            new_quiz.save()
                    count=count-counter
                return JsonResponse({"status": 'Добавил'}, status=200)
            else:
                return JsonResponse({"status": 'Некорректный ввод.Число должно быть больше 0!'}, status=200)
    elif request.method=='GET':
        return redirect('main_page')



class QuizViewSet(generics.ListAPIView):
    queryset = Quiz.objects.all().order_by('-data')
    serializer_class = QuizSerializer

