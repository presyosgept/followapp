from .models import Notification

def create_notification(employeeid, user, notification_type, extra_id):
    print("pangagaaawwwss moooooo")
    print(user)
    print(employeeid)
    print(extra_id)
    Notification.objects.create(to_user=employeeid, notification_type=notification_type, created_by=user, extra_id=extra_id)