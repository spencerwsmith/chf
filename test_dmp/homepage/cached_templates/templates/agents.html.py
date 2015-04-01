# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425351334.597493
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/agents.html'
_template_uri = 'agents.html'
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
        agents = context.get('agents', UNDEFINED)
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
        agents = context.get('agents', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Agents</title>\r\n\r\n\r\n<div class="clearfix"></div>\r\n<div class="text-right">\r\n    <a href="/homepage/agents.create/" class="btn btn-warning">Create New Agent</a>\r\n</div>\r\n\r\n <table id="agents_table" class ="table table-striped table-bordered table-hover">\r\n  <tr>\r\n      <th>User Name</th>\r\n      <th>First Name</th>\r\n      <th>Last Name</th>\r\n      <th>Email</th>\r\n      <th>Address 1</th>\r\n      <th>Address 2</th>\r\n      <th>City</th>\r\n      <th>State</th>\r\n      <th>ZIP</th>\r\n      <th>Security Question</th>\r\n      <th>Security Answer</th>\r\n      <th>Appointment Date</th>\r\n  </tr>\r\n')
        for agent in agents:
            __M_writer('    <tr>\r\n      <td> ')
            __M_writer(str( agent.username ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.first_name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.last_name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.email ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.address1 ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.address2 ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.city ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.state ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.zip ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.security_question ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.security_answer ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( agent.appointmentDate ))
            __M_writer('</td>\r\n      <td>\r\n          <a href="/homepage/agents.edit/')
            __M_writer(str( agent.id ))
            __M_writer('/">Edit</a>\r\n      </td>\r\n    </tr>\r\n')
        __M_writer(' </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/agents.html", "line_map": {"64": 34, "65": 34, "66": 35, "67": 35, "68": 36, "69": 36, "70": 37, "71": 37, "72": 38, "73": 38, "74": 39, "75": 39, "76": 40, "77": 40, "78": 41, "79": 41, "80": 43, "81": 43, "82": 47, "88": 82, "27": 0, "35": 1, "40": 49, "46": 3, "53": 3, "54": 28, "55": 29, "56": 30, "57": 30, "58": 31, "59": 31, "60": 32, "61": 32, "62": 33, "63": 33}, "uri": "agents.html"}
__M_END_METADATA
"""
