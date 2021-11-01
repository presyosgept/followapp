from .models import Notification

def create_notification(counselor, user, notification_type, extra_id, schedDay,schedStartTime,schedEndTime):
    Notification.objects.create(to_user=counselor, notification_type=notification_type, created_by=user, extra_id=extra_id,
    schedDay=schedDay, schedStartTime=schedStartTime, schedEndTime=schedEndTime  )