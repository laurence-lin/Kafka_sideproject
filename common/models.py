import json
from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class UserActivity:
    user_id: str
    event_type: str        # User action on APP：'login', 'logout', 'page_view', 'button_click'
    page: str              # APP webpage
    timestamp: str = None  # Timestamp when event occurs
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()
    
    def to_json(self):
        return json.dumps(asdict(self))
    
    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))