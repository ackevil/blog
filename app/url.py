from app.control.home import HomeControl
from app.control.post import PostControl
from app.control.voice import VoiceControl
url = [
    (r'/',HomeControl),
    (r'/s',HomeControl),
    (r'/t/([%a-zA-Z0-9]+)',HomeControl),
    (r'/p/([1-9][0-9]*)',PostControl),
    (r'/voice/([1-9][0-9]*)',VoiceControl)
]