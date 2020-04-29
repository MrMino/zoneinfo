__all__ = [
    "ZoneInfo",
    "reset_tzpath",
    "TZPATH",
    "ZoneInfoNotFoundError",
    "InvalidTZPathWarning",
]

from . import _tzpath
from ._common import ZoneInfoNotFoundError
from ._version import __version__

try:
    from ._czoneinfo import ZoneInfo
except ImportError:
    from ._zoneinfo import ZoneInfo

reset_tzpath = _tzpath.reset_tzpath
InvalidTZPathWarning = _tzpath.InvalidTZPathWarning


def __getattr__(name):
    if name == "TZPATH":
        return _tzpath.TZPATH
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(__all__ + ["__version__"])
