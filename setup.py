from setuptools import setup, find_packages

setup(
    name='riptide_db_mysql',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # TODO
    ],
    entry_points='''
        [riptide.db_driver]
        mysql=riptide_db_mysql.mysql:MySQLDbDriver
    ''',
)