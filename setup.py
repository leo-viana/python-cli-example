from setuptools import setup

setup(
    name='python-phrase',
    version='1.0.0',
    py_modules=['app'],
    install_requires=['Click', ],
    entry_points={
        'console_scripts': [
            'python-phrase = python-phrase:cli'
        ]
    })
