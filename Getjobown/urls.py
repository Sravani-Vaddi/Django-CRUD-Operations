"""
URL configuration for Getjobown project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# The error suggests that Django is unable to find the URL pattern named 'delete'. This typically occurs when the URL name used in the template does not match any of the defined URL patterns in your Django project's urls.py file.

# Make sure you have correctly defined the URL pattern for the delete view in your urls.py file. It should look something like this:

# python
# Copy code
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/', views.my_form_view, name='my_form_view'),
    # path('data/', views.Data),
    path('update/<int:pk>/', views.update_view, name='update'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),  # Ensure correct URL pattern
]