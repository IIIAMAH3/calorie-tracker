from django.shortcuts import render
from .models import Food, Consume


def index(request):
    if request.method == "POST":
        food_consumed = request.POST["food_consumed"]
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume_object = Consume(user=user, food_consumed=consume)
        consume_object.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    return render(request, "tracker/index.html", {"foods": foods})
