#!/usr/bin/env python3
#
# Copyright (c) 2021 Iliass Alami Qammouri
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import os
import socket
import sys

import requests
import sublist3r
from art import *
from termcolor import colored

from modules.dirsearchscan import dirsearch_scan
from modules.exit import exit
from modules.sublister import sublist3r_scan
from modules.sslscan import ssl_scan
from modules.niktoscan import nikto_scan
from modules.nmapscan import nmap_scan

ans = True
version = "0.0.1"
home = os.path.expanduser("~")


def re_open():
    installed = True if os.path.exists("/usr/local/bin/webmap") else False

    if installed:
        os.system("sudo webmap")
        sys.exit()

    else:
        os.system("sudo python3 webmap.py")
        sys.exit(())


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def not_valid(func, var, num=1):
    num = True
    if num == True:
        if len(var) <= 5:
            clear()

            print(
                colored("\nNot Valid Choice Try again\n",
                        "red",
                        attrs=["reverse"]))
            func()
    else:
        clear()

        print(
            colored("\nNot Valid Choice Try again\n", "red",
                    attrs=["reverse"]))
        func()


def dir_output(var, path, url):
    if len(var) == 0:
        var = path + "/" + url
        return var


def call_def(func, num=1):
    if num == True:
        clear()
        ans = True
        while ans:
            func()
    else:
        clear()
        func()
