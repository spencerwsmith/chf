# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425667222.902272
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp/homepage/templates/productcatalog.html'
_template_uri = 'homepage/templates/productcatalog.html/'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
        catalog_items = context.get('catalog_items', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
        catalog_items = context.get('catalog_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>products</title>\r\n\r\n')
        for Product in catalog_items:
            __M_writer('        <div>')
            __M_writer(str( Product.name ))
            __M_writer('</div>\r\n')
        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n<div class="item_container text-center">\r\n    <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Colonial Hat.jpg"/>\r\n    <div class="text-muted">Colonial Hat</div>\r\n    <div class="text-right">\r\n        <button data-pid="')
        __M_writer(str( product.id ))
        __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n    </div>\r\n</div>\r\n\r\n<div class="item_container text-center">\r\n    <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Miniature Liberty Bells.jpg"/>\r\n    <div class="text-muted">Miniature Liberty Bells</div>\r\n    <div class="text-right">\r\n    <button class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n    </div>\r\n</div>\r\n\r\n<div class="item_container text-center">\r\n    <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Printer Breeches.jpg"/>\r\n    <div class="text-muted">Breeches</div>\r\n    <div class="text-right">\r\n    <button class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n    </div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp/homepage/templates/productcatalog.html", "line_map": {"64": 20, "65": 23, "66": 23, "27": 0, "68": 28, "37": 1, "70": 36, "42": 44, "76": 70, "48": 3, "67": 28, "69": 36, "57": 3, "58": 7, "59": 8, "60": 8, "61": 8, "62": 10, "63": 20}, "source_encoding": "ascii", "uri": "homepage/templates/productcatalog.html/"}
__M_END_METADATA
"""
