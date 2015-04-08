# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428533581.763106
_enable_loop = True
_template_filename = 'C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/productcatalog.html'
_template_uri = 'productcatalog.html'
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
        catalog_items = context.get('catalog_items', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        catalog_items = context.get('catalog_items', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Products Available</title>\r\n<h6>Items for Purchase</h6>\r\n<table id="rentals_table" class="table table-striped table-bordered">\r\n    <tr>\r\n        <th>Name</th>\r\n        <th>Photo</th>\r\n        <th>Price</th>\r\n        <th>Description</th>\r\n        <th>Quantity</th>\r\n        <th>Action</th>\r\n    </tr>\r\n')
        for Product in catalog_items:
            __M_writer('  <tr>\r\n\r\n        <td><a href = "/homepage/')
            __M_writer(str(Product.id ))
            __M_writer('/">')
            __M_writer(str(Product.name))
            __M_writer('</a></td>\r\n    <td><center><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( Product.name))
            __M_writer('.jpg/" height="150" /></center></td>\r\n    <td>')
            __M_writer(str( Product.price ))
            __M_writer('</td>\r\n    <td>')
            __M_writer(str( Product.description ))
            __M_writer('</td>\r\n    <td><input id="qty')
            __M_writer(str( Product.id ))
            __M_writer('"type = "number" name="Quantity" min="1" value="1" max="400"/></td>\r\n    <td><button data-pid="')
            __M_writer(str( Product.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button></td>\r\n  </tr>\r\n')
        __M_writer('    </table>\r\n<br>\r\n<br>\r\n<br>\r\n<br>\r\n<br>\r\n<br>\r\n\r\n<h6>Items for Rental</h6>\r\n<table id="rentals_table" class="table table-striped table-bordered">\r\n    <tr>\r\n        <th>Name</th>\r\n        <th>Photo</th>\r\n        <th>Price Per Day</th>\r\n        <th>Replacement Price</th>\r\n        <th>Days</th>\r\n        <th>Action</th>\r\n    </tr>\r\n')
        for rental in rentals:
            __M_writer('  <tr>\r\n\r\n    <td><a href = "/homepage/rentals.detail/')
            __M_writer(str( rental.id ))
            __M_writer('/">')
            __M_writer(str(rental.name))
            __M_writer('</a></td>\r\n    <td><center><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( rental.name))
            __M_writer('.jpg/" height="150" /></center></td>\r\n    <td>')
            __M_writer(str(rental.price_per_day))
            __M_writer(' </td>\r\n    <td>')
            __M_writer(str(rental.replacement_price))
            __M_writer(' </td>\r\n    <td><input id="qty')
            __M_writer(str( rental.id ))
            __M_writer('"type = "number" name = "qty" value ="1" min="1" max="400"/></td>\r\n    <td><button data-pid="')
            __M_writer(str( rental.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button></td>\r\n  </tr>\r\n')
        __M_writer('</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "productcatalog.html", "filename": "C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/productcatalog.html", "line_map": {"27": 0, "37": 1, "42": 57, "48": 3, "57": 3, "58": 16, "59": 17, "60": 19, "61": 19, "62": 19, "63": 19, "64": 20, "65": 20, "66": 20, "67": 20, "68": 21, "69": 21, "70": 22, "71": 22, "72": 23, "73": 23, "74": 24, "75": 24, "76": 27, "77": 45, "78": 46, "79": 48, "80": 48, "81": 48, "82": 48, "83": 49, "84": 49, "85": 49, "86": 49, "87": 50, "88": 50, "89": 51, "90": 51, "91": 52, "92": 52, "93": 53, "94": 53, "95": 56, "101": 95}}
__M_END_METADATA
"""
