# -*- coding: utf-8 -*-
"""
    robo.handlers.talk
    ~~~~~~~~~~~~~~~~~~

    Talk.

    Porting from `ruboty-talk <https://github.com/negipo/ruboty-talk>`_.


    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import logging
from doco.client import Client as DocomoClient
from robo.decorators import cmd


class Client(object):
    def __init__(self):
        apikey = os.environ.get('DOCOMO_API_KEY', None)
        self.client = DocomoClient(apikey=apikey)
        self.options = None

    def talk(self, message):
        if self.options is None:
            res = self.client.send(utt=message, apiname='Dialogue')
        else:
            res = self.client.send(utt=message, apiname='Dialogue',
                                   **self.options)

        return res['utt']


class Talk(object):
    @property
    def options(self):
        return None

    @options.setter
    def options(self, options):
        if 'doco' in options:
            self.options = options['doco']

    def __init__(self):
        #: Change requests log level.
        logging.getLogger('requests').setLevel(logging.ERROR)
        logging.getLogger('doco').setLevel(logging.ERROR)
        self.client = Client()
        self.options = None

    @cmd(regex=r'.+',
         missing=True,
         description='Talk if given message didn\'t match any other handlers')
    def get(self, message, **kwargs):
        return self.client.talk(message.match.group(0))
