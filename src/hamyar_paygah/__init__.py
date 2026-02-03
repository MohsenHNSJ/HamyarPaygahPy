"""Hamyar Paygah.
--------------------------

Application for EMS overseers to gather information from EMS servers.

:copyright: (c) 2026-present MohsenHNSJ
:license: MIT, see LICENSE for more details

"""  # noqa: D205

__title__ = "HamyarPaygahPy"
__author__ = "MohsenHNSJ"
__license__ = "MIT"
__copyright__ = "Copyright 2026-present MohsenHNSJ"
__version__ = "0.2.1"

from . import main
from .app import paths
from .localization import language_manager
from .models import mission_model
from .new_ui.dialogs import server_config_dialog
from .services import missions_list_service, parsers
from .utils import text_utils

__all__: list[str] = [
    "language_manager",
    "main",
    "mission_model",
    "missions_list_service",
    "parsers",
    "paths",
    "server_config_dialog",
    "text_utils",
]
