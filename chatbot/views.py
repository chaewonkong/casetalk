import json


from django.shortcuts import render
from django.http import JsonResponse
from api.scraper import case_scraper
from django.views.decorators.csrf import csrf_exempt


def buttons(request):

	return JsonResponse({
		"message":{"text": "판례번호를 띄어쓰기 없이 입력해주세요"},
		})
	

@csrf_exempt
def message(request):

	case = case_scraper(request)

	if case:
		return JsonResponse({
			"message": {
				"text": request + "\n\n판시사항\n\n" + case[0] +
						"\n\n판결요지\n\n" + case[1] +
						"\n\n케이스노트에서 자세히 보기\n\n" + case[2]
				},
			})
	else:
		return JsonResponse({
			"message": {"text": "판례번호를 띄어쓰기 없이 검색해주세요"}
			})
