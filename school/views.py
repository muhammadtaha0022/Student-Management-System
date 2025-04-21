from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def dashboard(request):
    # unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    # unread_notification_count = unread_notification.count()
    return render(request, "student-dashboard.html")