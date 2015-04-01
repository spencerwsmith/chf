# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425746236.370132
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        def content():
            return render_content(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Users</title>\r\n\r\n\r\n<div class="clearfix"></div>\r\n<div class="text-right">\r\n    <a href="/homepage/users.create/" class="btn btn-warning">Create New User</a>\r\n</div>\r\n\r\n <table id="users_table" class ="table table-striped table-bordered table-hover">\r\n  <tr>\r\n      <th>User Name</th>\r\n      <th>First Name</th>\r\n      <th>Last Name</th>\r\n      <th>Email</th>\r\n      <th>Address 1</th>\r\n      <th>Address 2</th>\r\n      <th>City</th>\r\n      <th>State</th>\r\n      <th>ZIP</th>\r\n      <th>Security Question</th>\r\n      <th>Security Answer</th>\r\n  </tr>\r\n')
        for user in users:
            __M_writer('    <tr>\r\n      <td> ')
            __M_writer(str( user.username ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.email ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.address1 ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.address2 ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.city ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.state ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.zip ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.security_question ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( user.security_answer ))
            __M_writer('</td>\r\n      <td>\r\n          <a href="/homepage/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/">Edit</a>\r\n      </td>\r\n    </tr>\r\n')
        __M_writer(' </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/users.html", "source_encoding": "ascii", "line_map": {"64": 33, "65": 33, "66": 34, "67": 34, "68": 35, "69": 35, "70": 36, "71": 36, "72": 37, "73": 37, "74": 38, "75": 38, "76": 39, "77": 39, "78": 41, "79": 41, "80": 45, "86": 80, "27": 0, "35": 1, "40": 47, "46": 3, "53": 3, "54": 27, "55": 28, "56": 29, "57": 29, "58": 30, "59": 30, "60": 31, "61": 31, "62": 32, "63": 32}, "uri": "users.html"}
__M_END_METADATA
"""
