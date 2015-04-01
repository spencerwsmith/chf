# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423186149.923031
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/roles.html'
_template_uri = 'roles.html'
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
        roles = context.get('roles', UNDEFINED)
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
        roles = context.get('roles', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Roles</title>\r\n\r\n\r\n<div class="clearfix"></div>\r\n<div class="text-right">\r\n    <a href="/homepage/roles.create/" class="btn btn-warning">Create New Role</a>\r\n</div>\r\n\r\n <table id="roles_table" class ="table table-striped table-bordered table-hover">\r\n  <tr>\r\n      <th>Name</th>\r\n      <th>Type</th>\r\n  </tr>\r\n')
        for role in roles:
            __M_writer('    <tr>\r\n      <td> ')
            __M_writer(str( role.name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( role.type ))
            __M_writer('</td>\r\n      <td>\r\n          <a href="/homepage/roles.edit/')
            __M_writer(str( role.id ))
            __M_writer('/">Edit</a>\r\n      </td>\r\n    </tr>\r\n')
        __M_writer(' </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "roles.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/roles.html", "line_map": {"35": 1, "68": 62, "40": 29, "46": 3, "59": 21, "53": 3, "54": 18, "55": 19, "56": 20, "57": 20, "58": 21, "27": 0, "60": 23, "61": 23, "62": 27}, "source_encoding": "ascii"}
__M_END_METADATA
"""
