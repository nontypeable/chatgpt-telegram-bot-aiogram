import gettext
import os
from typing import Callable


def get_translation(language: str) -> Callable[..., str]:
    """method that makes it easier to work with multiple locales"""

    # defining an absolute path to locales
    locales_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "locales")

    translation = gettext.translation(domain="base", localedir=locales_path, languages=[language], fallback=True)

    return translation.gettext
