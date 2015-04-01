# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425678182.76314
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/myaccount.html'
_template_uri = 'myaccount.html'
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
        

        __M_writer('\r\n\r\n')
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
        __M_writer('\r\n\r\n<title>My Account</title>\r\n\r\n\r\n<div class="clearfix"></div>\r\n\r\n <table id="users_table" class ="table table-striped table-bordered table-hover">\r\n  <tr>\r\n      <th>User Name</th>\r\n      <th>First Name</th>\r\n      <th>Last Name</th>\r\n      <th>Email</th>\r\n      <th>Address 1</th>\r\n      <th>Address 2</th>\r\n      <th>City</th>\r\n      <th>State</th>\r\n      <th>ZIP</th>\r\n      <th>Security Question</th>\r\n      <th>Security Answer</th>\r\n  </tr>\r\n    <tr>\r\n      <td> ')
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
        __M_writer('</td>\r\n      <td>\r\n          <a href="/homepage/myaccount.editaccount/')
        __M_writer(str( user.id ))
        __M_writer('/">Edit Info</a>\r\n      </td>\r\n      <td>\r\n          <a href="/homepage/myaccountpass/')
        __M_writer(str( user.id ))
        __M_writer('/">Edit Password</a>\r\n      </td>\r\n    </tr>\r\n\r\n </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 30, "65": 30, "66": 31, "67": 31, "68": 32, "69": 32, "70": 33, "71": 33, "72": 34, "73": 34, "74": 35, "75": 35, "76": 37, "77": 37, "78": 40, "79": 40, "85": 79, "27": 0, "35": 1, "40": 46, "46": 3, "53": 3, "54": 25, "55": 25, "56": 26, "57": 26, "58": 27, "59": 27, "60": 28, "61": 28, "62": 29, "63": 29}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/myaccount.html", "uri": "myaccount.html"}
__M_END_METADATA
"""
