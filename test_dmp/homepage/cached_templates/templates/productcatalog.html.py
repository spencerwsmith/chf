# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428435725.560377
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
        def content():
            return render_content(context._locals(__M_locals))
        catalog_items = context.get('catalog_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
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
        catalog_items = context.get('catalog_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<title>Products Available</title>\r\n<h2>Items for Purchase:</h2>\r\n')
        for Product in catalog_items:
            __M_writer('        <a href="/homepage/')
            __M_writer(str( Product.id ))
            __M_writer('/">\r\n        <div class="item_container text-center text-muted">\r\n            <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( Product.name ))
            __M_writer('.jpg/"/>\r\n            <div>')
            __M_writer(str( Product.name ))
            __M_writer('</div>\r\n            <div>$')
            __M_writer(str( Product.price ))
            __M_writer('</div>\r\n            <div>')
            __M_writer(str( Product.description ))
            __M_writer('</div>\r\n            <div><input id="qty')
            __M_writer(str( Product.id ))
            __M_writer('"type = "number" name="Quantity" min="1" value="1" max="400"/></div>\r\n            <div class="text-right">\r\n                <button data-pid="')
            __M_writer(str( Product.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n            </div>\r\n        </div>\r\n        </a>\r\n')
        __M_writer('<br>\r\n<br>\r\n<br>\r\n<br>\r\n<br>\r\n<br>\r\n<div class="item_container text-center text-muted">\r\n    <h2>The following products are available for rental</h2>\r\n')
        for Rental_Product in rentals:
            __M_writer('        <div class="item_container text-center text-muted">\r\n            <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( Rental_Product.name ))
            __M_writer('.jpg/"/>\r\n            <a href="/homepage/productlist/">\r\n            <div>')
            __M_writer(str( Rental_Product.name ))
            __M_writer('</div>\r\n            <div>$')
            __M_writer(str( Rental_Product.price ))
            __M_writer('</div>\r\n            <div>')
            __M_writer(str( Rental_Product.description ))
            __M_writer('</div>\r\n            </a>\r\n            <div><input id="qty')
            __M_writer(str( Rental_Product.id ))
            __M_writer('"type = "number" name="Quantity" min="1" value="1" max="400"/></div>\r\n            <div class="text-right">\r\n                <button data-pid="')
            __M_writer(str( Rental_Product.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n            </div>\r\n        </div>\r\n        </a>\r\n')
        __M_writer('\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 12, "65": 12, "66": 13, "67": 13, "68": 14, "69": 14, "70": 15, "71": 15, "72": 16, "73": 16, "74": 18, "75": 18, "76": 23, "77": 31, "78": 32, "79": 33, "80": 33, "81": 33, "82": 33, "83": 35, "84": 35, "85": 36, "86": 36, "87": 37, "88": 37, "89": 39, "90": 39, "27": 0, "92": 41, "93": 46, "91": 41, "37": 1, "42": 50, "48": 4, "99": 93, "57": 4, "58": 9, "59": 10, "60": 10, "61": 10, "62": 12, "63": 12}, "uri": "productcatalog.html", "source_encoding": "ascii", "filename": "C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/productcatalog.html"}
__M_END_METADATA
"""
