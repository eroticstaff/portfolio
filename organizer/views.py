from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
import json

# Create your views here.
def index(request):
    new_cards = Card.objects.filter(status=0)
    in_progress_cards = Card.objects.filter(status=1)
    complete_cards = Card.objects.filter(status=2)
    context = {"new_cards": new_cards, "in_progress_cards": in_progress_cards, "complete_cards": complete_cards}
    return render(request, 'organizer/index.html', context=context)


def save_card(request):
    card_id = request.POST.get('card-id')
    card_name = request.POST.get('card-name')
    card_description = request.POST.get('card-description')
    card_tasks_json = request.POST.get('card-tasks')
    card = Card.objects.filter(id=card_id)
    card_tasks = json.loads(card_tasks_json)
    return HttpResponse(card_tasks[1])