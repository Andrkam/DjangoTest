from django.http import HttpResponse


def hello(request):
	return HttpResponse(f'<font size="10", color = "red">Если честно материала, который предоставляется на обучении очень мало, все бегло проходится. <br>'
	                    'Галопом по Европам как говорится<br>'
	                    'Прошу оценить мой немного кривой гороскоп)<br></font>'
	                    '<font size="12", color = "green">И задание от <b><font size="15">SkillFactory</font></b><br></font>'
	                    '<font size="14"><a href=/horoscope>Гороскоп</a></font>'
	                    '<br>'
	                    '<font size="14"><a href=/SkillFactory>SkillFactory</a></font>'
	                    )

