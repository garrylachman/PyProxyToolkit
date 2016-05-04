"""
Copyright (C) 2016 Garry Lachman garry@lachman.co under GNU LGPL
https://github.com/garrylachman/PyProxyToolkit
https://rev.proxies.online

This library is free software; you can redistribute it and/or modify it under the terms of the
GNU Lesser General Public License version 2.1, as published by the Free Software Foundation.

This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Lesser General Public License for more details.
"""

from distutils.core import setup

setup(
        name='PyProxyToolkit',
        version='0.0.9',
        packages=['PyProxyToolkit', 'PyProxyToolkit.strategies'],
        py_modules=['PyProxyToolkit.Console'],
        url='http://rev.proxies.online',
        license='GPL',
        author='Garry Lachman',
        author_email='garry@lachman.co',
        description='Python proxy checker toolkit'
)
