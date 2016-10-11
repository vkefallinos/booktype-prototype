
from .models import Activity





def create_activity(action, revision, ):
    new_activity = Activity(
        action=action,
    
        revision=revision,
    
    )
    new_activity.save()
    return new_activity










def delete_activity(activity_id):
    activity = Activity.objects.get(id=activity_id)
    activity.delete()
    return {"ok": True}








def get_activity(activity_id):
    return Activity.objects.get(id=activity_id)

def get_Activities():
    return Activity.objects.all()
