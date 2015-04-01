# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427831499.666578
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/login.html'
_template_uri = 'login.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n<a href="/homepage/logout/" class=" btn btn-success">Yes</a>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer("\r\n\r\n <form method='POST'>\r\n     <table>\r\n     ")
        __M_writer(str( form ))
        __M_writer('\r\n         <a href="/homepage/logout/" class=" btn btn-success">Yes</a>\r\n     </table>\r\n     <a href="/homepage/logout/" class=" btn btn-success">Yes</a>\r\n     <input type="submit"/>\r\n     <a href="/homepage/logout/" class=" btn btn-success">Yes</a>\r\n </form>\r\n<a href="/homepage/logout/" class=" btn btn-success">Yes</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "login.html", "line_map": {"35": 1, "53": 3, "54": 7, "55": 7, "40": 15, "27": 0, "61": 55, "46": 3}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/login.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
