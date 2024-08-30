from setuptools import setup

setup(
    name = 'backlog-analyzer',
    version = '0.1.0',
    packages = ['backloganalyzer'],
    entry_points = {
        'console_scripts': [
            'backloganalyzer = backloganalyzer.__main__:main'
        ]
    })
