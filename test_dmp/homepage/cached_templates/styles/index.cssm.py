# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422474232.706191
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\styles/index.cssm'
_template_uri = 'index.cssm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        timecolor = context.get('timecolor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('.server-time {\r\n  font-size: 2em;\r\n  color: ')
        __M_writer(str( timecolor ))
        __M_writer(';\r\n}\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\styles/index.cssm", "uri": "index.cssm", "line_map": {"16": 0, "24": 3, "30": 24, "22": 1, "23": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
