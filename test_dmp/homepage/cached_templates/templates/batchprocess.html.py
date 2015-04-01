# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427763115.3624
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/batchprocess.html'
_template_uri = 'batchprocess.html'
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
        sixty = context.get('sixty', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        zero = context.get('zero', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sixty = context.get('sixty', UNDEFINED)
        def content():
            return render_content(context)
        zero = context.get('zero', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<title>Overdue Rentals</title>\r\n\r\n<a href="/homepage/batchprocess.email/" class="btn btn-warning">Send Emails</a>\r\n  <table>\r\n   <tr>\r\n      <th>Renter\'s Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Rental Product</th>\r\n\r\n  </tr>\r\n\r\n')
        for Rented_Item in sixty:
            __M_writer('       <tr>\r\n           <h1>Items overdue by 60 days or more</h1>\r\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\r\n            <p></p>\r\n       </tr>\r\n')
        __M_writer("  </table>\r\n<br>\r\n<br>\r\n<br>\r\n\r\n <table>\r\n   <tr>\r\n      <h1>Items overdue between 30 and 60 days</h1>\r\n      <th>Renter's Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Rental Product</th>\r\n\r\n  </tr>\r\n\r\n")
        for Rented_Item in thirty:
            __M_writer('       <tr>\r\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\r\n            <p></p>\r\n       </tr>\r\n')
        __M_writer("  </table>\r\n<br>\r\n<br>\r\n<br>\r\n\r\n <table>\r\n   <tr>\r\n      <th>Renter's Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\r\n      <th>Rental Product</th>\r\n  </tr>\r\n\r\n")
        for Rented_Item in zero:
            __M_writer('       <tr>\r\n           <h1>Items overdue for 30 days or less</h1>\r\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\r\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\r\n            <p></p>\r\n       </tr>\r\n')
        __M_writer('  </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "batchprocess.html", "line_map": {"27": 0, "37": 1, "47": 4, "56": 4, "57": 18, "58": 19, "59": 21, "60": 21, "61": 22, "62": 22, "63": 23, "64": 23, "65": 24, "66": 24, "67": 25, "68": 25, "69": 29, "70": 45, "71": 46, "72": 47, "73": 47, "74": 48, "75": 48, "76": 49, "77": 49, "78": 50, "79": 50, "80": 51, "81": 51, "82": 55, "83": 69, "84": 70, "85": 72, "86": 72, "87": 73, "88": 73, "89": 74, "90": 74, "91": 75, "92": 75, "93": 76, "94": 76, "95": 80, "101": 95}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/batchprocess.html"}
__M_END_METADATA
"""
