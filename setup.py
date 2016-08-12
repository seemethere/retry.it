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

with open('README', 'r') as fp:
    retry_long_description = fp.read()

setup(
    name='retry',
    version=retry.__version__,
    author=retry.__author__,
    author_email='seemethere101@gmail.com',
    url='https://github.com/seemethere/retry',
    py_modules=['retry'],
    description='A small and simple library to retry functions',
    long_description=retry_long_description,
    license=retry.__license__,
    classifiers=retry_classifiers
)
