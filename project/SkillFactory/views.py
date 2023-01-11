from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
	return HttpResponse('Задания от SkillFactory <br><a href=/one> Задание № 1 - На одной из страниц контент повторяется 2 раза без изменения content (два раза прописано {{ flatpage.content }}). </a><br>'
	                    '<a href=/adminonly> Задание № 2 - Одна из страниц на сайте доступна только админу (только вошедшему пользователю) </a><br>'
	                    '<a href=/fontschange> Задание № 3 На одной из страниц изменены шрифты и размеры текста. </a><br>')