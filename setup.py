
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

with open('requirements.txt') as f: 
    requirements = f.readlines() 

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
        version ='1.2.1', 
)
