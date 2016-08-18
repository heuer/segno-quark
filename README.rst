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

One installed, the quark is automatically detected as `Segno`_ plugin and
therefore available via ``qrcode.to_XXX(...)``.


Available converters
--------------------

All converters use the same keyword parameters as Segno's SVG serializer,
see :py:method:`segno.QRCode.save()` for details.


ETree
^^^^^

Creates a SVG QR Code and returns the SVG document as
:py:class:`xml.etree.ElementTree`

Usage: ``to_etree``

This converter provides no additional keyword arguments.



Pacman
^^^^^^

Creates a QR Code with a smiley (and optional ghosts).

Usage: ``to_pacman``

===============     ============================================================
Keyword             Description
===============     ============================================================
pacman_color        Color of the smiley, default: ``#fc0``
dot_color           Color of the dots which the smiley should eat, default:
                    ``#fc0``
ghosts              Number of ghosts, default: ``5``. If set to ``0``, no ghost
                    appears. Note: Setting this a very high value may cause an
                    infinite loop iff number of ghosts > number of available
                    dark modules. Additionally, the QR Code may not be readable
                    by common QR Code decoders.
                    The positions of the ghosts are choosen at random.
ghost_colors        A tuple of colors which the ghosts may get. Default:
                    ``('#ff0c13', '#f2aeaf', '#1bb1e6', '#f97e16')``
                    Not all colors may be used, the colors for the ghosts are
                    choosen at random.
===============     ============================================================


Example:

.. code-block:: python

    >>> import segno
    >>> qr = segno.make_qr('Ob-La-Di, Ob-La-Da')
    >>> qr.to_pacman('obladioblada.svg', scale=10, ghosts=7)


Result:

.. image:: https://raw.githubusercontent.com/heuer/segno-quark/develop/imgs/pacman.svg
    :width: 495
    :height: 495



.. _Segno: https://github.com/heuer/segno
