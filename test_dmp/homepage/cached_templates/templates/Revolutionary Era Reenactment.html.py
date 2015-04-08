# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428473024.689661
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
        events = context.get('events', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        esi = context.get('esi', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Festivals</title>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        esi = context.get('esi', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h1>The Revolutionary Era Reenactment</h1>\r\n<h2> This event is perfect for all ages. Admission is free, so come have a fun time as you learn and gain a greater appreciation for those who came before us!</h2>\r\n<br>\r\n        <div class="item_container">\r\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/')
        __M_writer(str( events.name ))
        __M_writer('.jpg/"/>\r\n            <div>')
        __M_writer(str( events.name ))
        __M_writer('</div>\r\n            <div>')
        __M_writer(str( events.location ))
        __M_writer('</div>\r\n            <div>Event Start on: ')
        __M_writer(str( events.start_date ))
        __M_writer('</div>\r\n            <div>Event Ends on: ')
        __M_writer(str( events.end_date ))
        __M_writer('</div><br>\r\n            <div>')
        __M_writer(str( events.description ))
        __M_writer('</div>\r\n            <div class="text-right">\r\n            </div>\r\n        </div>\r\n\r\n<br><h3>Listed below are the main areas you can expect to visit at this event:</h3>\r\n\r\n        <div class="col-md-10">\r\n')
        for Area in areas:
            __M_writer('                <div class="col-md-4">\r\n                    <h2>Area: ')
            __M_writer(str( Area.aname ))
            __M_writer('</h2>\r\n                    <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/')
            __M_writer(str( Area.aname ))
            __M_writer('.jpg/"/>\r\n                    <h4></h4>\r\n                    <div>')
            __M_writer(str( Area.description ))
            __M_writer('</div>\r\n                    <h5>An expected sale item at ')
            __M_writer(str( Area.aname ))
            __M_writer(':</h5>\r\n')
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
            __M_writer('                    <br>\r\n                </div>\r\n')
        __M_writer('\r\n\r\n        </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/Revolutionary Era Reenactment.html", "line_map": {"27": 0, "38": 1, "48": 5, "58": 5, "59": 11, "60": 11, "61": 11, "62": 11, "63": 12, "64": 12, "65": 13, "66": 13, "67": 14, "68": 14, "69": 15, "70": 15, "71": 16, "72": 16, "73": 24, "74": 25, "75": 26, "76": 26, "77": 27, "78": 27, "79": 27, "80": 27, "81": 29, "82": 29, "83": 30, "84": 30, "85": 31, "86": 32, "87": 33, "88": 34, "89": 34, "90": 34, "91": 34, "92": 35, "93": 35, "94": 36, "95": 36, "96": 38, "97": 38, "98": 39, "99": 39, "100": 43, "101": 46, "107": 101}, "uri": "Revolutionary Era Reenactment.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
