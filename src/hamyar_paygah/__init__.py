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
__version__ = "0.1.4"

from . import main, missions_list_ui
from .app import paths
from .localization import language_manager
from .models import mission_model
from .services import missions_list_service, parsers
from .ui.dialogs import server_config_dialog
from .utils import text_utils

__all__: list[str] = [
    "language_manager",
    "main",
    "mission_model",
    "missions_list_service",
    "missions_list_ui",
    "parsers",
    "paths",
    "server_config_dialog",
    "text_utils",
]
