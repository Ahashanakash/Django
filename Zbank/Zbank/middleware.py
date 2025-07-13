import pytz
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Get timezone from cookie
        user_timezone = request.COOKIES.get('user_timezone')
        
        if user_timezone:
            try:
                # Set the timezone for this request
                timezone.activate(pytz.timezone(user_timezone))
            except pytz.exceptions.UnknownTimeZoneError:
                # If timezone is invalid, use UTC
                timezone.activate(pytz.UTC)
        else:
            # Default to UTC if no timezone cookie
            timezone.activate(pytz.UTC) 