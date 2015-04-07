# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428381644.878676
_enable_loop = True
_template_filename = 'C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/saleitems.html'
_template_uri = 'saleitems.html'
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
        saleitems = context.get('saleitems', UNDEFINED)
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
        saleitems = context.get('saleitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Sale Items</title>\r\n\r\n\r\n<div class="clearfix"></div>\r\n<div class="text-right">\r\n    <a href="/homepage/saleitems.create/" class="btn btn-warning">Create New Sale Item</a>\r\n</div>\r\n\r\n <table id="saleitems_table" class ="table table-striped table-bordered table-hover">\r\n  <tr>\r\n      <th>Sale Item</th>\r\n      <th>Description</th>\r\n      <th>Low Price</th>\r\n      <th>High Price</th>\r\n      <th>Area</th>\r\n  </tr>\r\n')
        for Expected_Sale_Item in saleitems:
            __M_writer('    <tr>\r\n      <td> ')
            __M_writer(str( Expected_Sale_Item.name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( Expected_Sale_Item.description ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( Expected_Sale_Item.low_price ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( Expected_Sale_Item.high_price ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( Expected_Sale_Item.area ))
            __M_writer('</td>\r\n      <td>\r\n          <a href="/homepage/saleitems.edit/')
            __M_writer(str( Expected_Sale_Item.id ))
            __M_writer('/">Edit</a>\r\n      </td>\r\n    </tr>\r\n')
        __M_writer(' </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 27, "65": 27, "66": 29, "35": 1, "68": 33, "40": 35, "74": 68, "46": 3, "59": 24, "67": 29, "53": 3, "54": 21, "55": 22, "56": 23, "57": 23, "58": 24, "27": 0, "60": 25, "61": 25, "62": 26, "63": 26}, "uri": "saleitems.html", "source_encoding": "ascii", "filename": "C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/saleitems.html"}
__M_END_METADATA
"""
