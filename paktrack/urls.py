"""App URLs"""

# Django
from django.urls import path

# AA PAK Track
# AA Example App
from paktrack import views

app_name: str = "paktrack"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.index, name="index"),
]
