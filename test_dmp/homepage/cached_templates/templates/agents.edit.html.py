# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423252866.314597
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/agents.edit.html'
_template_uri = 'agents.edit.html'
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
        form = context.get('form', UNDEFINED)
        agent = context.get('agent', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        agent = context.get('agent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  <form method="POST">\r\n   <table>\r\n    ')
        __M_writer(str( form ))
        __M_writer('\r\n   </table>\r\n    <button type="submit" class="\'btn btn-primary">Submit</button>\r\n    <a href ="/homepage/agents.delete/')
        __M_writer(str( agent.id ))
        __M_writer('/" class="btn btn-danger">Delete Agent</a>\r\n\r\n  </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/agents.edit.html", "line_map": {"64": 58, "36": 1, "54": 3, "55": 7, "56": 7, "57": 10, "58": 10, "27": 0, "46": 3}, "source_encoding": "ascii", "uri": "agents.edit.html"}
__M_END_METADATA
"""
