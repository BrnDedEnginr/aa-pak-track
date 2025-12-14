"""App Configuration"""

# Django
from django.apps import AppConfig

# AA PAK Track
# AA Example App
from paktrack import __version__


class PAKTrackConfig(AppConfig):
    """App Config"""

    name = "paktrack"
    label = "paktrack"
    verbose_name = f"PAK Track v{__version__}"
