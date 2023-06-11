from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    else:
        return localtime() - visit.entered_at


def format_duration(duration):
    duration_hours = duration.total_seconds() // 3600
    duration_minutes = (duration.total_seconds() % 3600) // 60
    return f'{int(duration_hours)} ч {int(duration_minutes)} мин'
