# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='drf-hal-json',
    version="0.10.0",
    url='https://github.com/seebass/drf-hal-json',
    license='MIT',
    description='Extension for Django REST Framework 3 which allows for using content-type application/hal-json',
    author='Sebastian Bredehöft',
    author_email='bredehoeft.sebastian@gmail.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'django>=2.0',
        'djangorestframework>=3.10.0',
        'drf-nested-fields>=0.9.0'
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
