# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428551483.477025
_enable_loop = True
_template_filename = 'C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/Revolutionary Era Reenactment.html'
_template_uri = 'Revolutionary Era Reenactment.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
        events = context.get('events', UNDEFINED)
        esi = context.get('esi', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        areas = context.get('areas', UNDEFINED)
        events = context.get('events', UNDEFINED)
        esi = context.get('esi', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Rev Era Festival</title>\r\n<h1>The Revolutionary Era Reenactment</h1>\r\n<h2> This event is perfect for all ages. Admission is free, so come have a fun time as you learn and gain a greater appreciation for those who came before us!</h2>\r\n<br>\r\n\r\n<table id="rentals_table" class="table table-condensed">\r\n    <tr>\r\n        <th><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/')
        __M_writer(str( events.name ))
        __M_writer('.jpg/"/></th>\r\n        <th>\r\n\r\n            ')
        __M_writer(str( events.name ))
        __M_writer('</div>\r\n            <div>')
        __M_writer(str( events.location ))
        __M_writer('</div><br>\r\n            <div>Event Start on: ')
        __M_writer(str( events.start_date ))
        __M_writer('</div>\r\n            <div>Event Ends on: ')
        __M_writer(str( events.end_date ))
        __M_writer('</div><br>\r\n            <div>')
        __M_writer(str( events.description ))
        __M_writer('</div>\r\n            <div class="text-right"></div>\r\n\r\n        </th>\r\n    </tr>\r\n</table>\r\n\r\n\r\n\r\n<br>\r\n<br>\r\n\r\n\r\n<table id="rentals_table" class="table table-striped table-bordered">\r\n    <tr>\r\n        <th>Area Name</th>\r\n        <th>Photo</th>\r\n        <th>Description</th>\r\n        <th>Expected Sale Items</th>\r\n    </tr>\r\n')
        for Area in areas:
            __M_writer('  <tr>\r\n    <td>Area: ')
            __M_writer(str( Area.aname ))
            __M_writer('</td>\r\n    <td><center> <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( Area.aname ))
            __M_writer('.jpg/"/></center></td>\r\n    <td>')
            __M_writer(str( Area.description ))
            __M_writer(' </td>\r\n    <td>\r\n')
            for Expected_Sale_Item in esi:
                if Area.aname == Expected_Sale_Item.area.aname:
                    __M_writer('                                <a href="http://localhost:8000/homepage/productcatalog/">\r\n                                <img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('homepage/media/')
                    __M_writer(str( Expected_Sale_Item.name ))
                    __M_writer('.jpg/"/>\r\n                                <div>')
                    __M_writer(str( Expected_Sale_Item.name ))
                    __M_writer('</div>\r\n                                <div>')
                    __M_writer(str( Expected_Sale_Item.description ))
                    __M_writer('</div>\r\n                                    </a>\r\n                                <div>Low Estimate: ')
                    __M_writer(str( Expected_Sale_Item.low_price ))
                    __M_writer('</div>\r\n                                <div>High Estimate: ')
                    __M_writer(str( Expected_Sale_Item.high_price ))
                    __M_writer('</div>\r\n\r\n')
            __M_writer('      </td>\r\n\r\n  </tr>\r\n')
        __M_writer('</table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/Revolutionary Era Reenactment.html", "uri": "Revolutionary Era Reenactment.html", "line_map": {"27": 0, "38": 1, "48": 3, "58": 3, "59": 12, "60": 12, "61": 12, "62": 12, "63": 15, "64": 15, "65": 16, "66": 16, "67": 17, "68": 17, "69": 18, "70": 18, "71": 19, "72": 19, "73": 39, "74": 40, "75": 41, "76": 41, "77": 42, "78": 42, "79": 42, "80": 42, "81": 43, "82": 43, "83": 45, "84": 46, "85": 47, "86": 48, "87": 48, "88": 48, "89": 48, "90": 49, "91": 49, "92": 50, "93": 50, "94": 52, "95": 52, "96": 53, "97": 53, "98": 57, "99": 61, "105": 99}, "source_encoding": "ascii"}
__M_END_METADATA
"""
