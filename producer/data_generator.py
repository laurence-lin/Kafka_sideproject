import random
from common.models import UserActivity

# Dummy user activity data value range
USER_IDS = [f"user_{i}" for i in range(1, 100)]  # Random users
EVENT_TYPES = ['login', 'logout', 'page_view', 'button_click', 'search', 'purchase']
PAGES = ['home', 'profile', 'products', 'cart', 'checkout', 'settings', 'help']

def generate_user_activity():
    """
    Random generate User Action data
    """
    user_id = random.choice(USER_IDS)
    event_type = random.choice(EVENT_TYPES)
    page = random.choice(PAGES)
    
    return UserActivity(
        user_id=user_id,
        event_type=event_type,
        page=page
    )