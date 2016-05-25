#
# otopi -- plugable installer
# Copyright (C) 2012-2014 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#


"""
This module contains constants used in this library.
"""


import re


NOTE_EVENT = 'note'
LOG_EVENT = 'log'
TERMINATE_EVENT = 'terminate'
QUERY_STRING_EVENT = 'query_string'
QUERY_MULTI_STRING_EVENT = 'query_multi_string'
QUERY_VALUE_EVENT = 'query_value'
CONFIRM_EVENT = 'confirm'
DISPLAY_VALUE_EVENT = 'display_value'
DISPLAY_MULTI_STRING_EVENT = 'display_multi_string'

TYPE_KEY = 'type'
REGEX_KEY = 'regex'
ATTRIBUTES_KEY = 'attributes'
REPLY_KEY = 'reply'
ABORT_KEY = 'abort'

TRANSLATION = (
    {
        TYPE_KEY: NOTE_EVENT,
        REGEX_KEY: re.compile(r'^#+ *(?P<note>.*)$'),
    },
    {
        TYPE_KEY: LOG_EVENT,
        REGEX_KEY: re.compile(
            r'^[*]{3}L:(?P<severity>[^ ]+) (?P<record>.*)$'
        ),
    },
    {
        TYPE_KEY: TERMINATE_EVENT,
        REGEX_KEY: re.compile(r'^[*]{3}TERMINATE$'),
    },
    {
        TYPE_KEY: QUERY_STRING_EVENT,
        REGEX_KEY: re.compile(r'^[*]{3}Q:STRING (?P<name>.*)$'),
    },
    {
        TYPE_KEY: QUERY_MULTI_STRING_EVENT,
        REGEX_KEY: re.compile(
            r'^[*]{3}Q:MULTI-STRING '
            r'(?P<name>[^ ]+) '
            r'(?P<boundary>[^ ]+) '
            r'(?P<abort_boundary>.+)$'
        ),
    },
    {
        TYPE_KEY: QUERY_VALUE_EVENT,
        REGEX_KEY: re.compile(r'^[*]{3}Q:VALUE (?P<name>.*)$'),
    },
    {
        TYPE_KEY: CONFIRM_EVENT,
        REGEX_KEY: re.compile(
            r'^[*]{3}CONFIRM (?P<what>[^ ]+) (?P<description>.*)$'
        ),
    },
    {
        TYPE_KEY: DISPLAY_VALUE_EVENT,
        REGEX_KEY: re.compile(
            r'^[*]{3}D:VALUE '
            r'(?P<name>[^=]+)='
            r'(?P<type>[^:]+):'
            r'(?P<value>.*)$'
        ),
    },
    {
        TYPE_KEY: DISPLAY_MULTI_STRING_EVENT,
        REGEX_KEY: re.compile(
            r'^[*]{3}D:MULTI-STRING (?P<name>[^ ]+) (?P<boundary>.*)$'
        ),
    },
)
