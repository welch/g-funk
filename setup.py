#!/usr/bin/env python
import os.path
from setuptools import setup

__version__ = "can't find version.py"
exec(compile(open('g-funk/version.py').read(), # pylint: disable=exec-used
                  'g-funk/version.py', 'exec'))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='g-funk',
      version=__version__,
      description='Whole-genome functional classification of genes via PCA',
      author='Will Welch',
      author_email='github@quietplease.com',
      packages=['g-funk'],
      license="MIT",
      keywords="Gene mapping, Principal Component Pursuit, Robust PCA",
      url="https://github.com/welch/g-funk",
      long_description=read('README.rst'),
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 2.7",
          "Topic :: Scientific/Engineering",
      ],
      install_requires=[
          "numpy",
      ],
      tests_require=[
          "pytest"
      ],
      setup_requires=[
          "pytest-runner"
      ],
      extras_require={
          "PLOT":  ["matplotlib"]
      },
      entry_points={
          "console_scripts": [
              # "g-funk.demo = g-funk.application:demo_cmd [PLOT]",
          ],
      }
)
