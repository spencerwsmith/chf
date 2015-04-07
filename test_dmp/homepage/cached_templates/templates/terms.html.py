# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428384212.730548
_enable_loop = True
_template_filename = 'C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/terms.html'
_template_uri = 'terms.html'
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
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<head lang="en">\r\n    <meta charset="UTF-8">\r\n\r\n')
        __M_writer('\r\n')
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title >Terms</title>\r\n\r\n\r\n<body>\r\n        By entering and browsing this site you agree to our <a href="http://localhost:8000/homepage/consent">terms of consent</a>\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"51": 7, "34": 1, "35": 6, "57": 51, "27": 0, "45": 7}, "uri": "terms.html", "source_encoding": "ascii", "filename": "C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/terms.html"}
__M_END_METADATA
"""
