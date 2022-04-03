from codecs import open
from os import path
from setuptools import setup, find_packages

basedir = path.abspath(path.dirname(__file__))
with open(path.join(basedir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read().replace('\r\n', '\n')

setup(
    name='sports_api',
    version='0.1.0',
    description='Sports API package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jeffrey McKay',
    author_email='jmckay0319@gmail.com',
    url='https://github.com/int-i/python-starter',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    license='MIT',
    keywords='python, template',
    python_requires='>=3',
)