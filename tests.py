# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 -- Lars Heuer - Semagia <http://www.semagia.com/>.
# All rights reserved.
#
# License: BSD License
#
"""\
Tests against Segno Quark.

:author:       Lars Heuer (heuer[at]semagia.com)
:organization: Semagia - http://www.semagia.com/
:license:      BSD License
"""
from __future__ import absolute_import, unicode_literals
import xml.etree.ElementTree as etree
import io
import segno

_SVG_NS = 'http://www.w3.org/2000/svg'


def _parse_xml(buff):
    """\
    Parses XML and returns the root element.
    """
    buff.seek(0)
    return etree.parse(buff).getroot()


def _find_svg_el(root, name):
    return root.find('{{{0}}}{1}'.format(_SVG_NS, name))


def _find_el_by_id(parent_el, id):
    res = [el for el in parent_el if el.attrib.get('id') == id]
    assert len(res) in (0, 1)
    return res[0] if res else None


def test_to_etree():
    qr = segno.make_qr('Segno')
    tree = qr.to_etree(scale=10, border=0, color='red')
    assert tree is not None
    root = tree.getroot()
    assert root is not None
    path = _find_svg_el(root, 'path')
    assert path is not None
    assert 'red' == path.attrib['stroke']
    assert 'scale(10)' == path.attrib['transform']


def test_to_pacman_zero_ghosts():
    qr = segno.make_qr('Segno')
    out = io.BytesIO()
    qr.to_pacman(out, color='red', ghosts=0)
    root = _parse_xml(out)
    print(etree.tostring(root))
    assert root is not None
    defs = _find_svg_el(root, 'defs')
    assert defs is not None
    # Assume that pacman is there if a cicle is there
    circle = _find_svg_el(defs, 'circle')
    assert circle is not None
    ghost = _find_el_by_id(defs, 'ghost')
    assert ghost is None


def test_to_pacman_ghosts():
    qr = segno.make_qr('Segno')
    out = io.BytesIO()
    qr.to_pacman(out, color='red', ghosts=5)
    root = _parse_xml(out)
    assert root is not None
    defs = _find_svg_el(root, 'defs')
    assert defs is not None
    # Assume that pacman is there if a cicle is there
    circle = _find_svg_el(defs, 'circle')
    assert circle is not None
    ghost = _find_el_by_id(defs, 'ghost')
    assert ghost is not None


def test_to_glow():
    qr = segno.make_qr('Segno')
    out = io.BytesIO()
    qr.to_glow(out)
    root = _parse_xml(out)
    assert root is not None
    defs = _find_svg_el(root, 'defs')
    assert defs is not None
    filter = _find_el_by_id(defs, 'segno-glow')
    assert filter is not None


def test_to_blur():
    qr = segno.make_qr('Segno')
    out = io.BytesIO()
    qr.to_blur(out)
    root = _parse_xml(out)
    assert root is not None
    defs = _find_svg_el(root, 'defs')
    assert defs is not None
    filter = _find_el_by_id(defs, 'segno-blur')
    assert filter is not None


if __name__ == '__main__':
    import pytest
    pytest.main(['-x', __file__])
