from django.http import Http404
from django.shortcuts import render, get_object_or_404

from timeslots.models import TimeSlot
from timeslots.forms import TimeSlotRequestForm


def home(request):
    print(request.session.session_key)
    available_times = TimeSlot.objects.all_future_available()

    times_by_date = {}
    for time in available_times:
        if time.date in times_by_date:
            times_by_date[time.date].append(time)
            times_by_date[time.date].sort(key=lambda item: item.begin_time)
        else:
            times_by_date[time.date] = [time]

    return render(request, 'home.html', {
        'times_by_date': times_by_date,
    })


def reserve(request, timeslot_id):
    timeslot = get_object_or_404(TimeSlot, id=timeslot_id)
    if not timeslot.get_reservation(request.session):
        raise Http404()
    if request.method == 'POST':
        form = TimeSlotRequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if form.cleaned_data['timeslot_id'] != timeslot_id:
                raise Http404()
            name = form.cleaned_data['name']
            email_address = form.cleaned_data['email_address']
            details = form.cleaned_data['details']

            timeslot.name = name
            timeslot.email_address = email_address
            timeslot.details = details

            timeslot.save()

            return render(request, 'thank_you.html', {
                'timeslot': timeslot,
            })
    else:
        form = TimeSlotRequestForm()

    return render(request, 'request.html', {
        'request_form': form,
        'timeslot_id': timeslot.id,
    })
