[![Build Status](https://travis-ci.org/konstantinfarrell/sitemap3.svg?branch=develop)](https://travis-ci.org/konstantinfarrell/sitemap3)
[![Coverage Status](https://coveralls.io/repos/github/konstantinfarrell/sitemap3/badge.svg?branch=develop)](https://coveralls.io/github/konstantinfarrell/sitemap3?branch=develop)

# Sitemap3

Sitemap3 is an async sitemap generation utility written in Python 3.5.
It currently generates a list of urls within a website and writes them to `sitemap.txt`

## Install

    pip install sitemap3

or

    git clone git@github.com:konstantinfarrell/sitemap3.git
    cd sitemap3
    python setup.py install

Don't forget a virtualenv

## Usage

    sitemap --u <url>
    sitemap --u <url> --w <output>

## TODO

- Add xml support
