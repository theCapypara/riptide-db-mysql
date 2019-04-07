from setuptools import setup, find_packages

setup(
    name='riptide_db_mysql',
    version='0.1',
    packages=find_packages(),
    description='TODO',  # TODO
    long_description='TODO',  # TODO
    install_requires=[
        'riptide_lib == 0.1',
        'schema >= 0.6'
    ],
    # TODO
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points='''
        [riptide.db_driver]
        mysql=riptide_db_mysql.mysql:MySQLDbDriver
    ''',
)
