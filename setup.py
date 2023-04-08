from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Logging module to enable orchestration on self-hosted applications'
LONG_DESCRIPTION = 'A logging-like module to be implemented on self-hosted applications that allows Orchestra to coordinate tasks and gather metadata'

# Setting up
setup(
    name="orchestra-logger",
    version=VERSION,
    author="Orchestra (Hugo Lu)",
    author_email="<hugo@getorchestra.io>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'logging', 'data', 'orchestration'],
    classifiers=[    ]
)
