import os
from setuptools import setup, find_packages

entry_points = '''
[zc.buildout]
default=zc.zdaemonrecipe:Recipe
'''

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description=(
        read('README.txt')
        + '\n' +
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('zc', 'zdaemonrecipe', 'README.txt')
        + '\n' +
        'Download\n'
        '**********************\n'
        )

open('doc.txt', 'w').write(long_description)

name = 'zc.zdaemonrecipe'
setup(
    name = name,
    version = '0.1',
    author = 'Jim Fulton',
    author_email = 'jim@zope.com',
    description = 'ZC Buildout recipe for zdaemon scripts',
    long_description=long_description,
    license = 'ZPL 2.1',
    
    entry_points=entry_points,
    packages = find_packages('.'),
    namespace_packages = ['zc'],
    extras_require = dict(test=['zdaemon']),
    install_requires = ['setuptools',
                        'zc.buildout', 'zc.recipe.egg',
                        'ZConfig'],
    zip_safe = False,
    )