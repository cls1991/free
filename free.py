# coding: utf8

"""
    Memory usage command for macOS.
"""

__version__ = '1.1.0'

import platform
import re

import click
import sh
from prettytable import PrettyTable


class MemoryUsage(object):
    """
    This information is from [Apple's support](https://support.apple.com/en-us/HT201538).

    :param wired: Information in RAM that can't be moved to the Mac's drive. The amount of "Wired memory" depends on
        the applications you are using.
    :param active: This information is in RAM and has recently been used.
    :param inactive: This information is in RAM but isn't actively being used, though it was recently used.
        For example, if you've been using Mail and then quit it, the RAM that Mail was using is marked as "Inactive
        memory". Inactive memory is available for use by another application, just like free memory. However,
        if you open Mail before its inactive memory is used by a different application,
        Mail will open quicker because its inactive memory is converted to active memory,
        instead of loading it from the slower drive.
    :param free: This is the amount of RAM that's not being used.
    :param total: The total physical memory.
    """

    def __init__(self, wired=0, active=0, inactive=0, free=0, total=0):
        self.wired = wired
        self.active = active
        self.inactive = inactive
        self.free = free
        self.total = total

    def parse_memory_usage(self):
        """
        Parse memory usage information.
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
        Show memory usage information.

        :param option: Display the memory usage information in 'kilobytes' unit.
        :return: A float that represents the memory for each item, in terms of the unit specified by *option*.
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


def _cb_helper(ctx, param, value, option):
    if not value or ctx.resilient_parsing:
        return None

    m = MemoryUsage()
    m.parse_memory_usage()
    m.show_memory_usage(option=option)
    ctx.exit()


def cb_bytes(ctx, param, value):
    return _cb_helper(ctx, param, value, 'b')


def cb_kilo(ctx, param, value):
    return _cb_helper(ctx, param, value, 'k')


def cb_mega(ctx, param, value):
    return _cb_helper(ctx, param, value, 'm')


def cb_giga(ctx, param, value):
    return _cb_helper(ctx, param, value, 'g')


def cb_tera(ctx, param, value):
    return _cb_helper(ctx, param, value, 't')


def cb_human(ctx, param, value):
    return _cb_helper(ctx, param, value, 'h')


def cb_si(ctx, param, value):
    return _cb_helper(ctx, param, value, 's')


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
        print('only macOS is supported.')
        ctx.exit()
    """Display amount of free and used memory in the system"""
    cb_kilo(ctx, 'kilo', True)


if __name__ == '__main__':
    cli()
