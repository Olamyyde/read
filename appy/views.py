from django.http import HttpResponse, response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challlenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"


    # response_data = """
    #     <ul>
    #         <li><a href="/challenges/january">January</a></li>
    #     </ul>  
    # """
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
    
    # return HttpResponseRedirect("/challenge/" + redirect_month)




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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Month not supported")
        