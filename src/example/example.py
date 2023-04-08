import sys
import logging

logger =logging.getLogger('Firstlogger')

version = sys.version_info[:2]

if version == (3, 9) or version == (3, 5):
    logger.warning(
        "sentry-sdk 2.0.0 will drop support for Python %s.",
        "{}.{}\nPlease upgrade to the latest version to continue receiving upgrades and bugfixes".format(*version)
    )

import inspect

def foo():
   print(inspect.stack()[0][3])
   print(inspect.stack()[1][3])  # will give the caller of foos name, if something called foo
   print(inspect.stack()[2][3])  # will give the caller of foos name, if something called foo

def cuntof():
    foo()

cuntof()
