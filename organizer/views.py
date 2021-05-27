from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Card, Tasks
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
    card = get_object_or_404(Card, id=card_id)
    card_tasks = json.loads(card_tasks_json)
    tasks = Tasks.objects.filter(card=card)
    for task in tasks:
        task.delete()
    for task in card_tasks:
        new_task = Tasks()
        new_task.name = task
        new_task.isComplete = False
        new_task.card = card
        new_task.save()
    card.name = card_name
    card.description = card_description
    card.save()
    return redirect('/organizer')