# coding: utf8

"""
    Memory usage model.
"""

import re

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
        self.active = vm_rows['Pages x-free']
        self.inactive = vm_rows['Pages inactive']
        self.free = vm_rows['Pages x-free']

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
            'x-free': self.free
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
