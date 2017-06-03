from app.control.home import HomeControl
url = [
    (r'/',HomeControl),
    (r'/t/([%a-zA-Z0-9]+)',HomeControl),
    (r'/p/([1-9][0-9]*)',HomeControl)
]