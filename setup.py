#!/usr/bin/env python

from distutils.core import setup

setup(
    name='bbq',
    version='0.1',
    author='Jonas Lundberg',
    author_email='jonas@5monkeys.se',
    packages=['bbq'],
    url='https://github.com/5monkeys/bbq',
    license='LICENSE.md',
    description='Tasty deploy recipes',
    long_description=open('README.md').read(),
    keywords=['fabric', 'cuisine', 'chef', 'puppet', 'ssh', 'bbq'],
    install_requires=['fabric', 'cuisine', 'revolver'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Clustering',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities'
    ],
)
