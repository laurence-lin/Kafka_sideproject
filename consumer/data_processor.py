from common.models import UserActivity

def process_user_activity(activity: UserActivity):
    """
    Parse and process reteieved UserActivity model's data and return.
    In production, we may make further ETL tasks and stored process data.
    
    """
    
    result = {
        "user_id": activity.user_id,
        "category": "navigation" if activity.event_type in ['page_view', 'login', 'logout'] else "interaction",
        "importance": "high" if activity.event_type in ['purchase', 'login'] else "normal"
    }
    
    return result