# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426620400.875521
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/product.html'
_template_uri = 'product.html'
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
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Products</title>\r\n\r\n')
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
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n<div class="text-right">\r\n    <a href="/homepage/product.create/" class="btn btn-warning">Create New Product</a>\r\n</div>\r\n\r\n <table id="products_table" class ="table table-striped table-bordered table-hover">\r\n  <tr>\r\n      <th>Product Name</th>\r\n      <th>Price</th>\r\n      <th>Description</th>\r\n      <th>Manufacturer</th>\r\n      <th>Average Cost</th>\r\n      <th>SKU</th>\r\n      <th>Order Form Name</th>\r\n      <th>Production Time</th>\r\n      <th>Category</th>\r\n  </tr>\r\n')
        for product in products:
            __M_writer('    <tr>\r\n      <td> ')
            __M_writer(str( product.name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( product.price ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( product.description ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( product.manufacturer ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( product.average_cost ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( product.sku ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( product.order_form_name ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( product.production_time ))
            __M_writer('</td>\r\n      <td> ')
            __M_writer(str( product.category ))
            __M_writer('</td>\r\n      <td>\r\n          <a href="/homepage/product.edit/')
            __M_writer(str( product.id ))
            __M_writer('/">Edit</a>\r\n      </td>\r\n    </tr>\r\n')
        __M_writer(' </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/product.html", "uri": "product.html", "source_encoding": "ascii", "line_map": {"64": 31, "65": 31, "66": 32, "67": 32, "68": 33, "69": 33, "70": 34, "71": 34, "72": 35, "73": 35, "74": 37, "75": 37, "76": 41, "82": 76, "27": 0, "35": 1, "40": 43, "46": 5, "53": 5, "54": 25, "55": 26, "56": 27, "57": 27, "58": 28, "59": 28, "60": 29, "61": 29, "62": 30, "63": 30}}
__M_END_METADATA
"""
