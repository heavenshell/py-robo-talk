# -*- coding: utf-8 -*-
"""
    robo.handlers.takl
    ~~~~~~~~~~~~~~~~~~

    Talk with you if given message didn't match any other handlers.


    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
from setuptools import setup, find_packages

requires = ['robo', 'doco']

app_name = 'robo.handlers.talk'

rst_path = os.path.join(os.path.dirname(__file__), 'README.rst')
description = ''
with open(rst_path) as f:
    description = f.read()

setup(
    name=app_name,
    version='0.0.1',
    author='Shinya Ohyanagi',
    author_email='sohyanagi@gmail.com',
    url='http://github.com/heavenshell/py-robo-cron',
    description='Talk with you if given message didn\'t match any other handlers.',
    long_description=description,
    license='BSD',
    platforms='any',
    namespace_packages=['robo'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    package_dir={'': '.'},
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
        'Topic :: Communications :: Conferencing'
    ],
    tests_require=['robo', 'doco', 'mock'],
    test_suite='tests'
)
