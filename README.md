# Wiring The Filesystem (WTF)

## Overview

* [![Documentation Status](https://readthedocs.org/projects/python-wiring-the-filesystem/badge/?style=flat)](https://readthedocs.org/projects/python-wiring-the-filesystem/)
* [![GitHub Actions Build Status](https://github.com/cosgroma/python-wiring-the-filesystem/actions/workflows/github-actions.yml/badge.svg)](https://github.com/cosgroma/python-wiring-the-filesystem/actions) 
* [![Coverage Status](https://codecov.io/gh/cosgroma/python-wiring-the-filesystem/branch/main/graphs/badge.svg?branch=main)](https://app.codecov.io/github/cosgroma/python-wiring-the-filesystem)
* [![PyPI Package latest release](https://img.shields.io/pypi/v/wiring-the-filesystem.svg)](https://pypi.org/project/wiring-the-filesystem) 
* [![PyPI Wheel](https://img.shields.io/pypi/wheel/wiring-the-filesystem.svg)](https://pypi.org/project/wiring-the-filesystem) 
* [![Supported versions](https://img.shields.io/pypi/pyversions/wiring-the-filesystem.svg)](https://pypi.org/project/wiring-the-filesystem) 
* [![Supported implementations](https://img.shields.io/pypi/implementation/wiring-the-filesystem.svg)](https://pypi.org/project/wiring-the-filesystem) 
* [![Commits since latest release](https://img.shields.io/github/commits-since/cosgroma/python-wiring-the-filesystem/v0.0.0.svg)](https://github.com/cosgroma/python-wiring-the-filesystem/compare/v0.0.0...main)

WTF (Wiring The Filesystem) is a directory analysis tool designed to visualize the intricate parent-child relationships in file hierarchies, particularly useful for software component directories. Using customizable mapping tables for file extensions, colors, and symbols, WTF helps engineers untangle the structure of complex projects with ease.

## Installation

```bash
pip install wiring-the-filesystem
```

You can also install the in-development version with:

```bash
pip install https://github.com/cosgroma/python-wiring-the-filesystem/archive/main.zip
```

## Documentation

The official documentation is hosted on [Read the Docs](https://python-wiring-the-filesystem.readthedocs.io/).

## Development

To run all the tests run:

```bash
tox
```

`PYTEST_ADDOPTS=--cov-append tox` will append coverage to an existing `.coverage` file.
