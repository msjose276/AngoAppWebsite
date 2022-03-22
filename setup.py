# setup.py
from setuptools import setup
setup(
   name="FOO"
   ...
   extras_require = {
       'dev': ['pylint'],
       'build': ['requests']
   }
   ...
)
