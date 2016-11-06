from setuptools import setup

__version__ = '1.3'
__author__ = 'Eli Uriegas'

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
    name='retry.it',
    version=__version__,
    author=__author__,
    author_email='seemethere101@gmail.com',
    url='https://github.com/seemethere/retry',
    py_modules=['retry'],
    description=description,
    long_description=description,
    license='MIT',
    classifiers=retry_classifiers,
    install_requires=['decorator'],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
)
