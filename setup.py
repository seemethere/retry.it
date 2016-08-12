from setuptools import setup

import retry

retry_classifiers = [
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
]

description = 'A small and simple library to retry functions'

setup(
    name='retry',
    version=retry.__version__,
    author=retry.__author__,
    author_email='seemethere101@gmail.com',
    url='https://github.com/seemethere/retry',
    py_modules=['retry'],
    description=description,
    long_description=description,
    license='MIT',
    classifiers=retry_classifiers,
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
)
