from setuptools import setup, find_packages

setup(
    name='riptide_db_mysql',
    version='0.1',
    packages=find_packages(),
    description='TODO',  # TODO
    long_description='TODO - Project will be available starting May/June',  # TODO
    install_requires=[
        'riptide_lib == 0.1',
        'schema >= 0.6'
    ],
    # TODO
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points='''
        [riptide.db_driver]
        mysql=riptide_db_mysql.mysql:MySQLDbDriver
    ''',
)
