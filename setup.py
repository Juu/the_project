import os
import sys
import subprocess
from setuptools import setup
from distutils.cmd import Command
import distutils

class Lint(Command):
    description = "Run pylint"
    user_options = [
        ('pylint-rcfile=', None, 'path to Pylint config file'),
    ]

    def initialize_options(self):
        self.pylint_rcfile = 'config/pylintrc'

    def finalize_options(self):
        if self.pylint_rcfile:
            assert os.path.exists(self.pylint_rcfile), (
                'Pylint config file %s does not exist.' % self.pylint_rcfile)

    def run(self):
        command = ['pylint']
        command.append('--rcfile=%s' % self.pylint_rcfile)
        command.append('./app')
        self.announce(
            'Running command: %s' % str(command),
            level=distutils.log.INFO)
        try:
            subprocess.check_call(command)
        except:
            sys.exit(1)

class Test(Command):
    description = "Run unittest"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = 'python -m unittest discover -v -s test/'.split(' ')
        self.announce(
            'Running command: %s' % str(command),
            level=distutils.log.INFO)
        try:
            subprocess.check_call(command)
        except:
            sys.exit(1)

class Bandit(Command):
    description = "Run bandit"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = 'bandit -r app/'.split(' ')
        self.announce(
            'Running command: %s' % str(command),
            level=distutils.log.INFO)
        try:
            subprocess.check_call(command)
        except:
            sys.exit(1)

class Start(Command):
    description = "Start your app"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = 'python main.py'.split(' ')
        try:
            subprocess.check_call(command)
        except:
            sys.exit(1)


setup(
    name = "app",
    version = "0.0.1",
    description = ("A python template app"),
    packages=['app'],
    cmdclass={
        'lint': Lint,
        'test': Test,
        'bandit': Bandit,
        'start': Start,
    }
)
