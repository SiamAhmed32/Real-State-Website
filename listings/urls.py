from django.urls import path
from listings.views import listings_list, listings_retrieve, listing_create, listing_update, listing_delete
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', listings_list),
    path('listings/<pk>/', listings_retrieve),
    path('create/', listing_create),
    path('listings/<pk>/edit/', listing_update),
    path('listings/<pk>/delete/', listing_delete),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

