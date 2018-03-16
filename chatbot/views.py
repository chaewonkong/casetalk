import json


from django.shortcuts import render
from django.http import JsonResponse
from api.scraper import case_scraper
from django.views.decorators.csrf import csrf_exempt


def buttons(request):

	return JsonResponse({
		"type": "buttons",
		"buttons": ['판례검색', ]
		})


@csrf_exempt
def message(request):
	json_str = (request.body).decode('utf-8')
	json_data = json.loads(json_str)
	request = json_data['content']

	if request =='판례검색':
		return JsonResponse({
			"message": {"text": "판례번호를 띄어쓰기 없이 입력해주세요"}
			})
	else:
		try:
			case = case_scraper(request)
		except:
			return JsonResponse({
				"message": {
				"text": "해당 판례를 찾을 수 없습니다.\n띄어쓰기에 유의해 다시 검색해주세요.\n\n 예) 98다22543"
				}
			})
		else:
			return JsonResponse({
				"message": {
					"text": request + "\n\n판시사항\n\n" + case[0] +
							"\n\n판결요지\n\n" + case[1] +
							"\n\n케이스노트에서 자세히 보기\n\n" + case[2]
					},
			})