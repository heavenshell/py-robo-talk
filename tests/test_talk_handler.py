# -*- coding: utf-8 -*-
"""
    robo.tests.test_talk_handler
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for robo.handlers.talk.


    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import logging
import requests
import simplejson as json
from mock import patch
from unittest import TestCase
from robo.robot import Robot
from robo.handlers.talk import Client, Talk


def dummy_response(m):
    response = requests.Response()
    response.status_code = 200
    data = {
        'context': 'D0yHgwljc_mhTPIGs--toQ',
        'utt': '\u30ac\u30c3', 'da': '0', 'yomi': '\u30ac\u30c3',
        'mode': 'dialog'
    }
    response._content = json.dumps(data)

    m.return_value = response


class NullAdapter(object):
    def __init__(self, signal):
        self.signal = signal
        self.responses = []

    def say(self, message, **kwargs):
        self.responses.append(message)
        return message


class TestClient(TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ['DOCOMO_API_KEY'] = 'foo'
        cls.client = Client()

    @patch('doco.requests.post')
    def test_generate_url(self, m):
        """ Client().talk() should response docomo dialogue response. """
        dummy_response(m)
        ret = self.client.talk('nullpo')
        self.assertEqual(ret, '\u30ac\u30c3')


class TestTalkHandler(TestCase):
    @classmethod
    def setUpClass(cls):
        logger = logging.getLogger('robo')
        logger.level = logging.ERROR
        cls.robot = Robot('test', logger)
        cls.robot.register_default_handlers()

        os.environ['DOCOMO_API_KEY'] = 'foo'
        talk = Talk()
        talk.signal = cls.robot.handler_signal
        method = cls.robot.parse_handler_methods(talk)
        cls.robot.handlers.extend(method)

        adapter = NullAdapter(cls.robot.handler_signal)
        cls.robot.adapters['null'] = adapter

    @patch('doco.requests.post')
    def test_should_talk(self, m):
        """ Talk().get() should response docomo dialogue response. """
        dummy_response(m)
        self.robot.handler_signal.send('test aaaa')
        self.assertEqual(self.robot.adapters['null'].responses[0],
                         '\u30ac\u30c3')

        self.robot.adapters['null'].responses = []
