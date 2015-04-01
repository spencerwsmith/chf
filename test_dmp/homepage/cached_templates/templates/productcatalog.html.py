# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427858491.7243
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/productcatalog.html'
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
        catalog_items = context.get('catalog_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        catalog_items = context.get('catalog_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<title>Products Available</title>\r\n<h2>Items for Purchase:</h2>\r\n')
        for Product in catalog_items:
            __M_writer('        <a href="/homepage/')
            __M_writer(str( Product.id ))
            __M_writer('/">\r\n        <div class="item_container text-center text-muted">\r\n            <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( Product.name ))
            __M_writer('.jpg/"/>\r\n            <a href="/homepage/productlist/">\r\n            <div>')
            __M_writer(str( Product.name ))
            __M_writer('</div>\r\n            <div>$')
            __M_writer(str( Product.price ))
            __M_writer('</div>\r\n            <div>')
            __M_writer(str( Product.description ))
            __M_writer('</div>\r\n            </a>\r\n            <div><input id="qty')
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
{"source_encoding": "ascii", "line_map": {"64": 12, "65": 12, "66": 14, "67": 14, "68": 15, "69": 15, "70": 16, "71": 16, "72": 18, "73": 18, "74": 20, "75": 20, "76": 25, "77": 33, "78": 34, "79": 35, "80": 35, "81": 35, "82": 35, "83": 37, "84": 37, "85": 38, "86": 38, "87": 39, "88": 39, "89": 41, "90": 41, "27": 0, "92": 43, "93": 48, "91": 43, "37": 1, "42": 52, "48": 4, "99": 93, "57": 4, "58": 9, "59": 10, "60": 10, "61": 10, "62": 12, "63": 12}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/productcatalog.html", "uri": "productcatalog.html"}
__M_END_METADATA
"""
