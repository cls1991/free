# coding: utf8

"""
    Memory usage command for macos.
"""

__version__ = '1.0'

import platform

import click

from core import stat


def cb_bytes(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = stat.MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='b')
    ctx.exit()


def cb_kilo(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = stat.MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage()
    ctx.exit()


def cb_mega(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = stat.MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='m')
    ctx.exit()


def cb_giga(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = stat.MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='g')
    ctx.exit()


def cb_tera(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = stat.MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='t')
    ctx.exit()


def cb_human(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = stat.MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='h')
    ctx.exit()


def cb_si(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = stat.MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='s')
    ctx.exit()


def cb_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    click.echo(__version__)
    ctx.exit()


@click.command()
@click.option('-b', '--bytes', callback=cb_bytes, is_flag=True, help='show output in bytes')
@click.option('-k', '--kilo', callback=cb_kilo, is_flag=True, help='show output in kilobytes')
@click.option('-m', '--mega', callback=cb_mega, is_flag=True, help='show output in megabytes')
@click.option('-g', '--giga', callback=cb_giga, is_flag=True, help='show output in gigabytes')
@click.option('--tera', callback=cb_tera, is_flag=True, help='show output in terabytes')
@click.option('-h', '--human', callback=cb_human, is_flag=True, help='show human-readable output')
@click.option('--si', callback=cb_si, is_flag=True, help='use powers of 1000 not 1024')
@click.option('-V', '--version', callback=cb_version, is_flag=True, help='output version information and exit')
@click.pass_context
def cli(ctx, **kwargs):
    if platform.system() != 'Darwin':
        print('only mac os is supported.')
        ctx.exit()
    """Display amount of free and used memory in the system"""
    cb_kilo(ctx, 'kilo', True)


def main():
    """
    :return:
    """
    cli()


if __name__ == '__main__':
    main()
