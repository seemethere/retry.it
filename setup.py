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
    author_email=retry.__email__,
    url=retry.__url__,
    py_modules=['retry'],
    description=description,
    long_description=description,
    license=retry.__license__,
    classifiers=retry_classifiers,
    test_requires=['pytest']
)
