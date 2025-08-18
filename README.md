<h1>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://riptide-docs.readthedocs.io/en/latest/_images/logo_dark.png">
  <img alt="Riptide" src="https://riptide-docs.readthedocs.io/en/latest/_images/logo.png" width="300">
</picture>
</h1>

[<img src="https://img.shields.io/github/actions/workflow/status/theCapypara/riptide-db-mysql/build.yml" alt="Build Status">](https://github.com/theCapypara/riptide-db-mysql/actions)
[<img src="https://readthedocs.org/projects/riptide-docs/badge/?version=latest" alt="Documentation Status">](https://riptide-docs.readthedocs.io/en/latest/)
[<img src="https://img.shields.io/pypi/v/riptide-db-mysql" alt="Version">](https://pypi.org/project/riptide-db-mysql/)
[<img src="https://img.shields.io/pypi/dm/riptide-db-mysql" alt="Downloads">](https://pypi.org/project/riptide-db-mysql/)
<img src="https://img.shields.io/pypi/l/riptide-db-mysql" alt="License (MIT)">
<img src="https://img.shields.io/pypi/pyversions/riptide-db-mysql" alt="Supported Python versions">

Riptide is a set of tools to manage development environments for web applications.
It's using container virtualization tools, such as [Docker](https://www.docker.com/)
to run all services needed for a project.

Its goal is to be easy to use by developers.
Riptide abstracts the virtualization in such a way that the environment behaves exactly
as if you were running it natively, without the need to install any other requirements
the project may have.

Riptide consists of a few repositories, find the
entire [overview](https://riptide-docs.readthedocs.io/en/latest/development.html) in the documentation.

## Database-Driver: MySQL

This repository implements the database driver interface of the Riptide library for use
with MySQL-compatible databases. This allows users to manage MySQL databases within
Riptide projects via the Riptide CLI.

## Documentation

The complete documentation for Riptide can be found at [Read the Docs](https://riptide-docs.readthedocs.io/en/latest/).
