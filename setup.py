# -*- coding: utf-8 -*-

from pyocto import __version__
import setuptools

requirements = []

setuptools.setup(
    name = 'pyocto',
    version = __version__,
    description = 'Octoprint API Library',
    author = 'Morten Trab',
    author_email = 'morten@trab.dk',
    license= 'MIT',
    url = 'https://github.com/mtrab/pyocto',
    packages=setuptools.find_packages(),
    install_requires=requirements,
)