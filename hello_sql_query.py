#!/usr/bin/env python

import click
from dblib.querydb import SelectN, find_max_price

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option("--n", default=5, help="Select first N rows in the table, default 5")
def query_firstn(n):
    """Select first N rows in the table"""
    SelectN(n)


@cli.command()
@click.option("--color", default="E", help="Color can be chosen from D,E,F,G,H,I,J")
def max_price(color):
    """Find max price for a color"""
    find_max_price(color)


# run the CLI
if __name__ == "__main__":
    cli()
