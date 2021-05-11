
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from importlib.metadata import version
import pathlib

here = pathlib.Path(__file__).parent.resolve()

with open('requirements.txt') as f: 
    requirements = f.readlines() 

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
        version ='1.2.2', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                "skb = skb.skb:main"
            ] 
        }
)
