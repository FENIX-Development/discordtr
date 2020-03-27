__title__ = 'discordtr'
__author__ = 'JaimiTR'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019-2020 JaimiTR'
__version__ = '0.9'

from collections import namedtuple
from .komutlar import Bilgi, Emoji, Bot, Embed, JSON
import logging

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=1, minor=3, micro=2, releaselevel='final', serial=0)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
