from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pdf_tools.urls')),  # Yeh line aapki app ko project se joregi
]