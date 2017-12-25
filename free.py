# coding: utf8

"""
    Memory usage command for macos.
"""

__version__ = '1.0.7'

import platform
import re

import click
import sh
from prettytable import PrettyTable


class MemoryUsage(object):

    def __init__(self, wired=0, active=0, inactive=0, free=0, total=0):
        """
        :param wired:
        :param active:
        :param inactive:
        :param free:
        :param total:
        """
        self.wired = wired
        self.active = active
        self.inactive = inactive
        self.free = free
        self.total = total

    def parse_memory_usage(self):
        """
        :return:
        """
        st = sh.grep(sh.sysctl('-a'), 'mem')
        vm = sh.vm_stat()
        pattern = re.compile(':[\s]+')
        st_lines = st.split('\n')
        st_rows = dict()
        for line in st_lines:
            t = line.strip()
            if t:
                row = pattern.split(t)
                st_rows[row[0]] = int(row[1])
        vm_lines = vm.split('\n')
        vm_rows = dict()
        for i, line in enumerate(vm_lines):
            # ignore header
            if i == 0:
                continue
            t = line.strip()
            if t:
                row = pattern.split(t)
                # page size of 4096 bytes
                vm_rows[row[0]] = int(row[1].strip('\.')) * 4096
        self.total = st_rows['hw.memsize']
        self.wired = vm_rows['Pages wired down']
        self.active = vm_rows['Pages free']
        self.inactive = vm_rows['Pages inactive']
        self.free = vm_rows['Pages free']

    def show_memory_usage(self, option='k'):
        """
        :param option:
        :return:
        """
        memory = {
            'total': self.total,
            'wired': self.wired,
            'active': self.active,
            'inactive': self.inactive,
            'free': self.free
        }
        uc = 1024
        if option == 'b':
            uc = 1
        elif option == 'm':
            uc = 1024 * 1024
        elif option == 'g':
            uc = 1024 * 1024 * 1024
        elif option == 't':
            uc = 1024 * 1024 * 1024 * 1024
        elif option == 's':
            uc = 1000
        elif option == 'h':
            uc = 1024 * 1024 * 1024 * 1.0

        for field in memory:
            t = memory[field] / uc
            if option == 'h':
                s = '{:.1f}G'.format(t)
                memory[field] = s
            else:
                memory[field] = t
        pt = PrettyTable(memory.keys())
        pt.add_row(memory.values())
        print(pt)


def cb_bytes(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='b')
    ctx.exit()


def cb_kilo(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage()
    ctx.exit()


def cb_mega(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='m')
    ctx.exit()


def cb_giga(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='g')
    ctx.exit()


def cb_tera(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='t')
    ctx.exit()


def cb_human(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option='h')
    ctx.exit()


def cb_si(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    m = MemoryUsage()
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


if __name__ == '__main__':
    cli()
