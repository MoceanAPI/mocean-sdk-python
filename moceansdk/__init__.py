#!/usr/bin/env python
# -*- coding: utf-8 -*-
from moceansdk.auth import AbstractAuth
from moceansdk.auth.basic import Basic
from moceansdk.exceptions import MoceanErrorException, RequiredFieldException
from moceansdk.modules import Transmitter

name = "moceansdk"


class Client(object):
    SDK_VERSION = '1.0.2'

    def __init__(self, obj_auth, options=None):
        if not isinstance(obj_auth, AbstractAuth):
            raise MoceanErrorException("auth object must extend AbstractAuth")

        if obj_auth.get_auth_method().lower() == 'basic':
            if not obj_auth.get_params()['mocean-api-key'] or not obj_auth.get_params()['mocean-api-secret']:
                raise RequiredFieldException("Api key and api secret for client object can't be empty.")
        else:
            raise MoceanErrorException("unsupported auth method")

        if options is None or isinstance(options, dict):
            self._transmitter = Transmitter(options)
        else:
            self._transmitter = options
        self._obj_auth = obj_auth

    @property
    def sms(self):
        from moceansdk.modules.message.sms import Sms
        return Sms(self._obj_auth, self._transmitter)

    @property
    def flash_sms(self):
        from moceansdk.modules.message.sms import Sms
        __sms = Sms(self._obj_auth, self._transmitter)
        return __sms.set_mclass(1).set_alt_dcs(1)

    @property
    def balance(self):
        from moceansdk.modules.account.balance import Balance
        return Balance(self._obj_auth, self._transmitter)

    @property
    def pricing(self):
        from moceansdk.modules.account.pricing import Pricing
        return Pricing(self._obj_auth, self._transmitter)

    @property
    def message_status(self):
        from moceansdk.modules.message.message_status import MessageStatus
        return MessageStatus(self._obj_auth, self._transmitter)

    @property
    def verify_request(self):
        from moceansdk.modules.message.verify_request import VerifyRequest
        return VerifyRequest(self._obj_auth, self._transmitter)

    @property
    def verify_validate(self):
        from moceansdk.modules.message.verify_validate import VerifyValidate
        return VerifyValidate(self._obj_auth, self._transmitter)

    @property
    def number_lookup(self):
        from moceansdk.modules.number_lookup.number_lookup import NumberLookup
        return NumberLookup(self._obj_auth, self._transmitter)
