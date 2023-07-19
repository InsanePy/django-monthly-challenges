from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "This works in january",
    "february": "This works in february",
    "march": "This works in march",
    "april": "This works in april",
    "may": "This works in may",
    "june": "This works in june",
    "july": "This works in july",
    "august": "This works in august",
    "september": "This works in september",
    "october": "This works in october",
    "november": "This works in november",
    "december": None,
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


#   return HttpResponseRedirect("/challenge/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "title": "Monthly Challenge",
            "month_name": month,
            "text": challenge_text,

        })

    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
