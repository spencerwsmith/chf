# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426628550.39522
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/productlist.html'
_template_uri = 'productlist.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<title>Products List</title>\r\n\r\n')
        for Product in catalog_items:
            __M_writer('        <div class="item_container text-center text-muted">\r\n            <a href="/homepage/productcatalog/">\r\n            <div>')
            __M_writer(str( Product.name ))
            __M_writer('</div>\r\n            </a>\r\n            <div class="text-right">\r\n            </div>\r\n        </div>\r\n')
        __M_writer('\r\n\r\n\r\n<!--<div class="item_container text-center">\r\n    <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/breeches.jpg"/>\r\n    <div class="text-muted">Breeches</div>\r\n    <div class="text-right">\r\n    <button class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n    </div>\r\n</div>-->\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp\\homepage\\templates/productlist.html", "uri": "productlist.html", "source_encoding": "ascii", "line_map": {"68": 62, "27": 0, "36": 1, "41": 30, "47": 4, "55": 4, "56": 9, "57": 10, "58": 12, "59": 12, "60": 18, "61": 22, "62": 22}}
__M_END_METADATA
"""
