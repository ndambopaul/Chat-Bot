# custom_session_middleware.py

from django.utils import timezone
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions.backends.db import SessionStore

class CustomSessionMiddleware(SessionMiddleware):
    
    def process_request(self, request):
        super().process_request(request)
        
        last_activity = request.session.get('last_activity')
        if last_activity:
            expiration_time = last_activity + timezone.timedelta(seconds=settings.SESSION_COOKIE_AGE)
            if timezone.now() > expiration_time:
                request.session.flush()  # Clear session data if expired
                request.session['last_activity'] = timezone.now()
        else:
            request.session['last_activity'] = timezone.now()
