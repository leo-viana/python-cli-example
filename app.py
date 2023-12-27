#!/usr/bin/env python

import click

@click.group()
def cli():
    pass

@cli.command()
def quote():
    """Prints the phrase 'This is a test!'"""
    click.echo("This is a test!")

if __name__ == '__main__':
    cli()
