from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def announcement_list(request):
    announcements = [
        {'id': 1, 'title': 'Meeting Reminder', 'content': 'Team meeting at 3PM.'},
        {'id': 2, 'title': 'Holiday Notice', 'content': 'No classes on Monday!'},
    ]
    return render(request, 'announcements/list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcements = [
        {'id': 1, 'title': 'Meeting Reminder', 'content': 'Team meeting at 3PM.'},
        {'id': 2, 'title': 'Holiday Notice', 'content': 'No classes on Monday!'},
    ]
    announcement = next((a for a in announcements if a['id'] == id), None)
    if announcement:
        return render(request, 'announcements/detail.html', {'announcement': announcement})
    else:
        return render(request, 'announcements/not_found.html', status=404)
