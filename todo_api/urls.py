from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view to handle requests to the root URL
def index(request):
    return HttpResponse("Welcome to the Todo API! Access the API at /api/.")

urlpatterns = [
    path('', index),  # Handles the root URL
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),  # The API URLs are under /api/
]
