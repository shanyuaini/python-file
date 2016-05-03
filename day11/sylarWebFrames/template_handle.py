#_*_coding:utf-8_*_
__author__ = 'sylar'

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('app', 'templates'))

