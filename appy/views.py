from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.
# def index(request):
#     return HttpResponse("Working")

# def celeb(request):
#     return HttpResponse("fresh")

monthly_challenges = {
    "january": "Working",
    "february": "fresh",
    "march": "tanguy",
    "april": "tanguy",
    "may": "tanguy",
    "june": "tanguy",
    "july": "tanguy",
    "august": "tanguy",
    "september": "tanguy",
    "october": "tanguy",
    "november": "tanguy",
    "december": "defa",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)



# def challenge(request, month):
#     challenge_text = None
#     if month == "jan":
#         challenge_text = "Working"
#     elif month == "feb":
#         challenge_text = "fresh"
#     elif month == "march":
#         challenge_text = "Tan"
#     else:
#         return HttpResponseNotFound("Method not supported")
#     return HttpResponse(challenge_text)

def challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Month not supported")
        