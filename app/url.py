from app.control.home import HomeControl
from app.control.post import PostControl
url = [
    (r'/',HomeControl),
    (r'/t/([%a-zA-Z0-9]+)',HomeControl),
    (r'/p/([1-9][0-9]*)',PostControl)
]