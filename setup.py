from distutils.core import setup
from setuptools import find_packages

def get_version():
    return '2.0.1'

def get_requirements():
    with open('requirements.txt', 'rU') as fhan:
        requires = [line.strip() for line in fhan.readlines()]
    return requires

def get_long_description():
    try:
        import pypandoc
        long_description = pypandoc.convert('README.md', 'rst')
    except (IOError, ImportError):
        with open('README.txt') as fhan:
            long_description = fhan.read()
    return long_description


add_keywords = dict(
    entry_points={
        'console_scripts': ['universal = universal.main:main'],
    }, )

setup(
    name='Universal',
    description='Universal Competitive Programming Suite helps you work'
    ' faster in programming competitions',
    version=get_version(),
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                    "tests"]),
    license='GPLv3+',
    author='Shubham Chaudhary',
    author_email='me@shubhamchaudhary.in',
    url='https://github.com/shubhamchaudhary/universal',
    long_description=get_long_description(),
    install_requires=get_requirements(),
    **add_keywords)
