from django.shortcuts import render

from timeslots.models import TimeSlot


def home(request):
    available_times = TimeSlot.objects.all_future_available()

    times_by_date = {}
    for time in available_times:
        if time.date in times_by_date:
            times_by_date[time.date].append(time)
            times_by_date[time.date].sort(key=lambda item: item.begin_time)
        else:
            times_by_date[time.date] = [time]

    print(times_by_date)

    return render(request, 'home.html', {
        'times_by_date': times_by_date,
    })
