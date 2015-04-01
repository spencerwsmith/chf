# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425351793.921765
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Events</title>\r\n\r\n\r\n<div class="clearfix"></div>\r\n<div class="text-right">\r\n    <a href="/homepage/events.create/" class="btn btn-warning">Create New Event</a>\r\n</div>\r\n\r\n <table id="events_table" class ="table table-striped table-bordered table-hover">\r\n  <tr>\r\n      <th>Event Name</th>\r\n      <th>Start Date</th>\r\n      <th>End Date</th>\r\n      <th>Location Name</th>\r\n  </tr>\r\n')
        for event in events:
            __M_writer('    <tr>\r\n      <td> ')
            __M_writer(str( event.name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( event.start_date ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( event.end_date ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( event.location ))
            __M_writer('</td>\r\n      <td>\r\n          <a href="/homepage/events.edit/')
            __M_writer(str( event.id ))
            __M_writer('/">Edit</a>\r\n      </td>\r\n    </tr>\r\n')
        __M_writer(' </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "events.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/events.html", "line_map": {"64": 27, "65": 27, "66": 31, "35": 1, "40": 33, "46": 3, "59": 23, "72": 66, "53": 3, "54": 20, "55": 21, "56": 22, "57": 22, "58": 23, "27": 0, "60": 24, "61": 24, "62": 25, "63": 25}}
__M_END_METADATA
"""
