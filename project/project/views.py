from django.http import HttpResponse
from django.urls import reverse


def hello(request):
	return HttpResponse(f'<font size="12", color = "red">Если честно материала, который предоставляется на обучении очень мало, все бегло проходится. <br>'
	                    'Я сделал немного по другому и совсем другое задание. Но сделал)<br>'
	                    'По моему задание даже гдето сложнее. Прошу оценить мой немного кривой гороскоп)<br></font>'
	                    '<br>'
	                    '<br>'
	                    '<font size="14"><a href=/horoscope>Гороскоп</a></font>')