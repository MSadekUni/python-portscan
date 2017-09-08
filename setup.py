"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'python-portscan',

  version = '3.0.0',

  description = "A complex wrapper around the nmap command line utility.",

  long_description = long_description,

  url = 'https://github.com/DanielThurau/Kali_Port_Scanning',

  author = 'Daniel Thurau',

  author_email = 'Daniel.N.Thurau@gmail.com',

  license = 'BSD',

  classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Pick your license as you wish (should match "license" above)
     'License :: BSD License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],

  keywords = 'scanning vulnerability',

  packages = ['portscan'],

  install_requires = [
    'arrow',
    'yattag',
    'dropbox',
    'python-libnmap',
    'requests',
  ],

  python_requires = '>=3',



)
