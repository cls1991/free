# coding: utf8

"""
    Memory usage command for macos.
"""

__version__ = '1.0.dev0'

import click


def cb_bytes(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: bytes')
    ctx.exit()


def cb_kilo(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: kilo')
    ctx.exit()


def cb_mega(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: mega')
    ctx.exit()


def cb_giga(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: giga')
    ctx.exit()


def cb_tera(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: tera')
    ctx.exit()


def cb_human(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: human')
    ctx.exit()


def cb_si(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: si')
    ctx.exit()


def cb_lohi(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: lohi')
    ctx.exit()


def cb_old(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: old')
    ctx.exit()


def cb_total(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('@TODO: total')
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
@click.option('-l', '--lohi', callback=cb_lohi, is_flag=True, help='show detailed low and high memory statistics')
@click.option('-o', '--old', callback=cb_old, is_flag=True, help='use old format (without -/+buffers/cache line)')
@click.option('-t', '--total', callback=cb_total, is_flag=True, help='show total for RAM + swap')
@click.option('-V', '--version', callback=cb_version, is_flag=True, help='output version information and exit')
@click.pass_context
def cli(ctx, **kwargs):
    """Display amount of free and used memory in the system"""
    cb_kilo(ctx, 'kilo', True)


def main():
    """
    :return:
    """
    cli()


if __name__ == '__main__':
    main()
