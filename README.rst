###################################################
Automatically updated list of valid TLDs for Python
###################################################

The `tlds` module provides a a set of valid TLDs directly taken from IANA_. The package is automatically updated daily.

Available on PyPI_.

.. _IANA: http://data.iana.org/TLD/tlds-alpha-by-domain.txt
.. _PyPI: https://pypi.org/pypi/tlds/

.. image:: https://github.com/kichik/tlds/workflows/tlds%20build/badge.svg
   :alt: Build status
   :target: https://github.com/kichik/tlds/actions

.. image:: https://img.shields.io/pypi/v/tlds?logo=pypi
   :alt: PyPI
   :target: https://pypi.org/pypi/tlds/

.. image:: https://img.shields.io/pypi/dm/tlds?color=red
   :alt: PyPI - Downloads
   :target: https://pypi.org/pypi/tlds/

Usage
-----

  >>> from tlds import tld_set
  >>> 'com' in tld_set
  True
  >>> 'foobar' in tld_set
  False
  >>> 'pizza' in tld_set
  True
  >>>
