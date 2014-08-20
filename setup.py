#!/usr/bin/python

from setuptools import setup, find_packages

import mptt_tree_widget

author = mptt_tree_widget.__author__
github_url = 'https://github.com/beholderrk/mptttreewidget'
long_desc = open('README.md').read()

setup(
    name='mptt_tree_widget',
    version='0.0.1',
    description='javascript tree widget for mptt',
    long_description=long_desc,
    url=github_url,
    author=author,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    package_data={
        'mptt_tree_widget': [
            'templates/*.html',
            'static/admin/js/*.js',
            'static/jquery-treeview/*.css',
            'static/jquery-treeview/*.js',
            'static/jquery-treeview/images/*.gif',
        ]
    },
)
