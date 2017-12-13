# coding: utf8

"""
    Memory usage command for macos.
"""

import click


@click.command()
@click.option('-b', help='show output in bytes')
@click.option('-k', help='show output in kilobytes')
@click.option('-m', help='show output in megabytes')
@click.option('-g', help='show output in gigabytes')
@click.option('-h', help='show human-readable output')
@click.option('-l', help='show detailed low and high memory statistics')
@click.option('-o', help='use old format (without -/+buffers/cache line)')
@click.option('-t', help='show total for RAM + swap')
@click.option('-V', help='output version information and exit')
def cli():
    """
    :return:
    """
    pass


if __name__ == '__main__':
    cli()
