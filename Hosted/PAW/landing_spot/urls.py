from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URL patterns for the landing page for owner
    path('', views.owner_portfolio, name='landing_page'),
    
    # URL patterns for the landing page for other users
    path('portfolio/<str:username>', views.other_portfolio, name='landing_page'),
    
    # URL pattern for saving contact messages
    path('save_contact_message/<str:username>', views.save_contact_message, name='save_contact_message'),
    
    # URL pattern for project details
    path('project/<str:username>/<str:slug>', views.Project_Details, name='Project_Details'),   
]


# Serve static and media files in development
# This is only for development purposes. In production, you should use a proper web server.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
