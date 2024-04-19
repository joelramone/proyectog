# middleware.py
from .models import RequestLog

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Registra la solicitud en la base de datos
        RequestLog.objects.create(
            url=request.path,
            method=request.method,
            body=request.body
        )
        return self.get_response(request)
