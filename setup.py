#!/usr/bin/env python3

from setuptools import setup

setup(name='bistrobot',
      version='1.0',
      description='Raspi Zero GPIO controlled cat feeding robot',
      author='Maxence Ardouin',
      author_email='max@23.tf',
      url='https://github.com/nbr23/bistrobot',
      license='MIT',
      zip_safe=True,
      packages=['bistrobot'],
      install_requires=['gpiozero', 'RPi.GPIO'],
      entry_points={'console_scripts': [
          'bistrobot = bistrobot.__main__:main'
          ]},
      )
