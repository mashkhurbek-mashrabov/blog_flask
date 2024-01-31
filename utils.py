from flask import session, redirect

LOGIN_URL = "/login"


def login_required(function=None, redirect_url: str = None, login_url: str = LOGIN_URL):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """

    def view_wrapper(*args, **kwargs):
        if not "user" in session:
            return redirect(redirect_url or login_url)
        return function(*args, **kwargs)

    return view_wrapper
