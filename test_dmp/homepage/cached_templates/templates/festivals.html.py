# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427509463.136608
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/festivals.html'
_template_uri = 'festivals.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Festivals</title>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h1>Upcoming Festivals!</h1>\r\n\r\n')
        for Event in events:
            __M_writer('        <div class="item_container text-center">\r\n            <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( Event.name ))
            __M_writer('.jpg/"/>\r\n            <a href="http://localhost:8000/homepage/')
            __M_writer(str( Event.name ))
            __M_writer('">\r\n            <div>')
            __M_writer(str( Event.name ))
            __M_writer('</div>\r\n            </a>\r\n            <div>')
            __M_writer(str( Event.location ))
            __M_writer('</div>\r\n            <div>Event Start on: ')
            __M_writer(str( Event.start_date ))
            __M_writer('</div>\r\n            <div>Event Ends on: ')
            __M_writer(str( Event.end_date ))
            __M_writer('</div><br>\r\n            <div>')
            __M_writer(str( Event.description ))
            __M_writer('</div>\r\n            <div class="text-right">\r\n            </div>\r\n        </div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/festivals.html", "uri": "festivals.html", "line_map": {"64": 13, "65": 15, "66": 15, "67": 16, "68": 16, "69": 17, "70": 17, "71": 18, "72": 18, "73": 23, "79": 73, "27": 0, "36": 1, "46": 5, "54": 5, "55": 9, "56": 10, "57": 11, "58": 11, "59": 11, "60": 11, "61": 12, "62": 12, "63": 13}}
__M_END_METADATA
"""
