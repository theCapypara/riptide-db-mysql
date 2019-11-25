from setuptools import setup, find_packages

# README read-in
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
# END README read-in

setup(
    name='riptide-db_mysql',
    version='0.3.4',
    packages=find_packages(),
    description='Tool to manage development environments for web applications using containers - MySQL Database Drvier',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/Parakoopa/riptide-db-mysql/',
    install_requires=[
        'riptide-lib >= 0.3, < 0.4',
        'schema >= 0.7'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points='''
        [riptide.db_driver]
        mysql=riptide_db_mysql.mysql:MySQLDbDriver
    ''',
)
