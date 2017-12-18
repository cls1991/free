# coding: utf8


import subprocess


def execute(cmd):
    out = None
    if cmd:
        try:
            out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        except ValueError:
            pass

    return out


def test_env():
    print(execute(['pip', 'freeze']))


def test_free():
    assert execute(['free'])


def test_free_b():
    assert execute(['free', '-b']) and execute(['free', '--bytes'])


def test_free_k():
    assert execute(['free', '-k']) and execute(['free', '--kilo'])


def test_free_m():
    assert execute(['free', '-m']) and execute(['free', '--mega'])


def test_free_g():
    assert execute(['free', '-g']) and execute(['free', '--giga'])


def test_free_tera():
    assert execute(['free', '--tera'])


def test_free_h():
    assert execute(['free', '-h']) and execute(['free', '--human'])


def test_free_si():
    assert execute(['free', '--si'])


def test_free_version():
    assert execute(['free', '-V']) and execute(['free', '--version'])


def test_free_help():
    assert execute(['free', '--help'])
