from common.models import UserActivity

def process_user_activity(activity: UserActivity):
    """处理用户行为数据"""
    
    # 实际应用中，这里可以做更复杂的处理，如:
    # - 统计用户活跃度
    # - 分析用户行为路径
    # - 存储到数据库
    # - 实时计算用户指标
    
    result = {
        "user_id": activity.user_id,
        "category": "navigation" if activity.event_type in ['page_view', 'login', 'logout'] else "interaction",
        "importance": "high" if activity.event_type in ['purchase', 'login'] else "normal"
    }
    
    return result