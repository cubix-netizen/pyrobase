# pylint: disable=missing-docstring, bad-whitespace
""" Iterator Helper tests.

    Copyright (c) 2011-2020 The PyroScope Project <pyroscope.project@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
from __future__ import absolute_import, print_function, unicode_literals

import pytest

from pyrobase import iterutil


def yielding():
    yield 1
    yield (2, "3")


@pytest.mark.parametrize('val, expected', [
    ([],                []),
    ((1, "2"),          [1, "2"]),
    (yielding(),        [1, 2, "3"]),
    ((1, ["2", [], 3]), [1, "2", 3]),
])
def test_iterutil_flatten(val, expected):
    result = list(iterutil.flatten(val))
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
