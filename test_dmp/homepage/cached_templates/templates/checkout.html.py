# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427860311.567389
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/checkout.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
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
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if user.is_authenticated() :
            __M_writer('    <form>\r\n    <div>\r\n    <strong>Please enter your shipping and credit card information</strong><br>\r\n\r\n    First name:\r\n           <p></p> <input type="text" name="firstname"><br>\r\n    Last name:\r\n            <p></p><input type="text" name="lastname"><br>\r\n    Street Address:\r\n            <p></p><input type="text" name="firstname"><br>\r\n    City:\r\n            <p></p><input type="text" name="lastname"><br>\r\n    State:\r\n            <p></p><input type="text" name="firstname"><br>\r\n    Zip Code:\r\n            <p></p><input type="text" name="lastname"><br><br>\r\n    Credit Cart Number:\r\n            <p></p><input type="text" name="firstname"><br>\r\n    Security Code:\r\n           <p></p> <input type="text" name="lastname"><br>\r\n\r\n        <a href="/homepage/purchase" class="btn btn-default">Purchase</a>\r\n    </div>\r\n    </form>\r\n')
        else:
            __M_writer('       <div id="login">\r\n            <strong>You will need to login first in order to checkout, thank you.</strong>\r\n       </div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 3, "53": 6, "54": 7, "55": 31, "56": 32, "57": 36, "27": 0, "45": 3, "63": 57}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/checkout.html", "source_encoding": "ascii", "uri": "checkout.html"}
__M_END_METADATA
"""
