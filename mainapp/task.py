from celery import shared_task

# from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from users.models import User
from plyer import notification


# created a task which will run every hour
@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"


@shared_task
def send_desktop_notifications():
    notification_title = "GREETINGS !"
    notification_message = "Thank you. Have a Good Day."

    notification.notify(
        title=notification_title,
        message=notification_message,
        app_icon=None,
        timeout=10,
        toast=False,
    )
    online_users = User.objects.filter(is_online=True)
    channel_layer = get_channel_layer()
    print(channel_layer)

    for user in online_users:
        async_to_sync(channel_layer.group_send)(
            f"user_{user.username}",
            {"type": "send_notification", "message": "Notification message"},
        )
    return "Done"
