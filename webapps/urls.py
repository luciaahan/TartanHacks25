"""
URL configuration for webapps project.

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
from django.urls import path
from plan4me import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.global_action, name='home'),
    path('get-started', views.get_started_action, name='get-started'),
    path('personalize', views.personalize_action, name='personalize'),
    path('generate-schedule', views.generate_schedule_action, name='generate-schedule'),
    path('aboutUs', views.show_us_action, name='aboutUs'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
