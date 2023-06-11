from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.getting_duration import get_duration, format_duration


def storage_information_view(request):
    visit = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for human_info in visit:
        duration = get_duration(human_info)
        non_closed_visits.append({
            'who_entered': human_info.passcard,
            'entered_at': human_info.entered_at,
            'duration': format_duration(duration),
            'is_strange': Visit.is_visit_long(human_info)
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
