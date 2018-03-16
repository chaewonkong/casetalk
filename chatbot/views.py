from django.shortcuts import render
from django.http import JsonResponse


def keyboard(request):

	return JsonResponse({})


def message(request):

	return JsonResponse({
		"message": {
			"text": "판례번호를 띄어쓰기 없이 입력해주세요"
		},
		})
