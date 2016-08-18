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
see `segno.QRCode.save()`_ for details.


ETree
^^^^^

Creates a SVG QR Code and returns the SVG document as ``xml.etree.ElementTree``.

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

.. image:: https://raw.githubusercontent.com/heuer/segno-quark/master/images/pacman.png
    :alt: Example of to_pacman result
    :width: 495
    :height: 495



Glow
^^^^

Creates a QR Code with a "glow" effect.

Usage: ``to_glow``

===============     ============================================================
Keyword             Description
===============     ============================================================
filter_id           Indicates the id of the filter, default: ``segno-glow``
deviation           Indicates the standard deviation for the blur operation,
                    default: ``.6``
===============     ============================================================


Example:

.. code-block:: python

    >>> import segno
    >>> qr = segno.make_qr('Ob-La-Di, Ob-La-Da')
    >>> qr.to_glow('obladioblada.svg', scale=10, color='darkblue')


Result:

.. image:: https://raw.githubusercontent.com/heuer/segno-quark/master/images/glow.png
    :alt: Example of to_glow result
    :width: 330
    :height: 330


Blur
^^^^

Creates a QR Code with a "blur" effect.

Usage: ``to_blur``

===============     ============================================================
Keyword             Description
===============     ============================================================
filter_id           Indicates the id of the filter, default: ``segno-blur``
deviation           Indicates the standard deviation for the blur operation,
                    default: ``.3``
===============     ============================================================


Example:

.. code-block:: python

    >>> import segno
    >>> qr = segno.make_qr('Ob-La-Di, Ob-La-Da')
    >>> qr.to_blur('obladioblada.svg', scale=10, color='darkred')


Result:

.. image:: https://raw.githubusercontent.com/heuer/segno-quark/master/images/blur.png
    :alt: Example of to_blur result
    :width: 330
    :height: 330


.. _Segno: https://github.com/heuer/segno
.. _segno.QRCode.save(): https://segno.readthedocs.io/en/latest/api.html#segno.QRCode.save
