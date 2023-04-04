from django.urls import path
from api.views import VisitedDomainsView, VisitedLinksView

app_name = 'api'
urlpatterns = [
    path('visited_domains', VisitedDomainsView.as_view(), name='visited_domains'),
    path('visited_links', VisitedLinksView.as_view(), name='visited_links')
]