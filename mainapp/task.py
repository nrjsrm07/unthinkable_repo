from celery import shared_task

# created a task which will run every hour
@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"
