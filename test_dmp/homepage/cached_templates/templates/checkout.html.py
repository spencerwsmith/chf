# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428003164.03573
_enable_loop = True
_template_filename = 'C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if user.is_authenticated() :
            __M_writer('\r\n    <form method="POST">\r\n   <table>\r\n    ')
            __M_writer(str( form ))
            __M_writer('\r\n   </table>\r\n    <br>\r\n    <button type="submit" class="btn btn-primary">Purchase</button>\r\n\r\n  </form>\r\n\r\n\r\n')
        else:
            __M_writer('       <div id="login">\r\n            <strong>You will need to login first in order to checkout, thank you.</strong>\r\n       </div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "36": 1, "46": 3, "67": 61, "54": 3, "55": 6, "56": 7, "57": 10, "58": 10, "59": 18, "60": 19, "61": 23}, "uri": "checkout.html", "filename": "C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/checkout.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
