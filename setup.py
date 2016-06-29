#!/usr/bin/env python

import os
import sys
import pip

from pip.req import parse_requirements

from setuptools import find_packages, setup

version = "0.1.3"
description = 'sms communication for churches, built with django'

setup(name='apostello-cli',
      version=version,
      description=description,
      long_description=description,
      author='monty5811',
      author_email='montgomery.dean97@gmail.com',
      url='https://github.com/monty5811/apostello-docker-cli',
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'click<0.7',
          'docker-compose>=1.7',
          'semantic_version<2.6',
      ],
      license='MIT',
      zip_safe=False,
      classifiers=[
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
      ],
      keywords=('Python, twilio, sms, church, django, '),
      entry_points='''
        [console_scripts]
    apostello=ap_cli.main:cli
    ''', )
