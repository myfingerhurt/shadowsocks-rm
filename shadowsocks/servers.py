#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015 mengskysama
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import, division, print_function, \
    with_statement


import sys
import os
import logging
import _thread
import config
import getopt
import signal
import time


if config.LOG_ENABLE:
    if config.LOG_LEVEL == logging.DEBUG:
        logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%Y/%m/%d %a %H:%M:%S',filename=config.LOG_FILE,level=config.LOG_LEVEL)
    else:
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',datefmt='%Y/%m/%d %a %H:%M:%S',filename=config.LOG_FILE,level=config.LOG_LEVEL)


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from shadowsocks import shell, daemon, eventloop, tcprelay, udprelay, \
    asyncdns, manager
from shadowsocks.common import to_bytes, to_str

import manager
from dbtransfer import DbTransfer

def handler_SIGQUIT():
    return

def print_servers_help():
    print('''usage: ssserver [OPTION]...
shadowsocks manyusers branch

Proxy options:
  -s, --dns-server SERVER_ADDR         DNS server address, default: 8.8.8.8


General options:
  -h, --help             show this help message and exit
  --version              show version information

''')

def main():
    configer = {
        'server': '%s' % config.SS_BIND_IP,
        'local_port': 1081,
        'port_password': {
        },
        'method': '%s' % config.SS_METHOD,
        'manager_address': '%s:%s' % (config.MANAGE_BIND_IP, config.MANAGE_PORT),
        'timeout': 185, # some protocol keepalive packet 3 min Eg bt
        'fast_open': False,
        'verbose': 1
    }
    
<<<<<<< HEAD
    shortopts = 'h:s:'
    longopts = ['help', 'dns-server=', 'version']
=======
    shortopts = 'h:s'
    longopts = ['help', 'dns-server', 'version']
>>>>>>> 0785a877b6605ca1b76aea95304fcd901b9db933
    
    optlist, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
    for key, value in optlist:
        if key in ('-s', '--dns-server'):
<<<<<<< HEAD
            configer['dns_server'] = to_str(value)
            logging.info('dns input %s', value)
=======
            config['dns_server'] = to_str(value)
>>>>>>> 0785a877b6605ca1b76aea95304fcd901b9db933
        elif key in ('-h', '--help'):
            print_servers_help()
            sys.exit(0)
        elif key == '--version':
            print_shadowsocks()
            sys.exit(0)
<<<<<<< HEAD
        else:
            print_servers_help()
            sys.exit(0)

    
    t = thread.start_new_thread(manager.run, (configer,))
=======
    
    t = _thread.start_new_thread(manager.run, (configer,))
>>>>>>> 0785a877b6605ca1b76aea95304fcd901b9db933
    time.sleep(1)
    t = _thread.start_new_thread(DbTransfer.thread_db, ())
    time.sleep(1)
    t = _thread.start_new_thread(DbTransfer.thread_push, ())

    while True:
        time.sleep(100)


if __name__ == '__main__':
    main()
