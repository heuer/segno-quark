Segno Quark: Plugin for creating more advanced SVG documents
============================================================

This (experimental) `Segno`_ plugin changes the default SVG output in
different ways (i.e. applying SVG filters).

Tested under PyPy, Python 2.7 and Python 3.4. Unlike Segno itself, this
package does not work with Python 2.6.


Installation
------------

Use ``pip`` to install this quark from PyPI::

    $ pip install segno


Usage
-----

One installed, the quark is automatically detected by `Segno`_.

.. code-block:: python

    >>> import segno
    >>> qr = segno.make_qr('Ob-La-Di, Ob-La-Da')
    >>> qr.to_pacman('obladioblada.svg', ghosts=7)



.. _Segno: https://github.com/heuer/segno
