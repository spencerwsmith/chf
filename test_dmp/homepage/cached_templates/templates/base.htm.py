# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427935518.134447
_enable_loop = True
_template_filename = 'C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8" >\r\n  <meta name="description" content="The Colonial Heritage Foundation is an educational group organized in order to increase education and appreciation for the history of the United States of America. The foundation features history reenactments, exhibits and items for sale">\r\n  <meta name="keywords" content="history, reenactment, purchase, colonial, festival, revolutionary, America, gifts, educational"\r\n  <head>\r\n\r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <!-- Latest compiled and minified JavaScript -->\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n      <!-- Latest compiled and minified CSS -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\r\n    <!-- Optional theme -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css">\r\n\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n\r\n\r\n  <body>\r\n\r\n\r\n<nav class="navbar navbar-inverse">\r\n\r\n      <p class="navbar-text">Colonial Heritage Foundation</p><br><br><br>\r\n\r\n        <div name = "links" class="nav nav-pills nav-justified">\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/index" class="glyphicon glyphicon-home"> Home</a>\r\n            <li role="presentation"> <a href="http://localhost:8000/homepage/contact" class="glyphicon glyphicon-envelope"> Contact</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/terms" class="glyphicon glyphicon-book"> Terms</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/about" class="glyphicon glyphicon-list-alt"> About</a>\r\n')
        if request.user.is_authenticated():
            __M_writer('                <li role="presentation"><a href="http://localhost:8000/homepage/checkout/" class="glyphicon glyphicon-tags"> Checkout</a>\r\n                <li role="presentation"><a id="show_logout_dialog"> Logout</a>\r\n                <li role="presentation"><a id="cart"> Shopping Cart</a>\r\n')
        else:
            __M_writer('                <li role="presentation"><a id="show_login_dialog">Login</a>\r\n                <li role="presentation"><a href="http://localhost:8000/homepage/createaccount.create/" class="glyphicon glyphicon-plus-sign"> Create Account</a>\r\n')
        __M_writer('\r\n\r\n        </div>\r\n</nav>\r\n\r\n<div class="row">\r\n    <div class="col-md-2">\r\n        <ul class="nav nav-pills nav-stacked">\r\n\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/users" class="glyphicon glyphicon-user"> Users</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/agents" class="glyphicon glyphicon-star"> Agents</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/roles" class="glyphicon glyphicon-star-empty"> Roles</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/events" class="glyphicon glyphicon-bullhorn"> Events</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/product" class="glyphicon glyphicon-gift"> Products</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/productcatalog" class="glyphicon glyphicon-gift"> Products Available</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/productlist" class="glyphicon glyphicon-gift"> Product List</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/saleitems" class="glyphicon glyphicon-shopping-cart"> SaleItems</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/festivals" class="glyphicon glyphicon-leaf"> Festivals</a>\r\n')
        if request.user.is_authenticated():
            __M_writer('            <li role="presentation"><a href="http://localhost:8000/homepage/myaccount" class="glyphicon glyphicon-user"> My Account</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/batchprocess" class="glyphicon glyphicon-exclamation-sign"> Overdue Rentals</a>\r\n            <li role="presentation"><a href="http://localhost:8000/homepage/rentalreturn" class="glyphicon glyphicon-random"> rentalreturn</a>\r\n')
        __M_writer('        </ul>\r\n     </div>\r\n\r\n\r\n    <div class="col-md-10">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n    </div>\r\n  </div>\r\n  </body>\r\n</html>\r\n\r\n')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <title>homepage</title>\r\n            <div class="row">\r\n\r\n             <div >\r\n\r\n            Site content will go here\r\n\r\n             </div>\r\n            </div>\r\n\r\n\r\n         ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Spencer\\Documents\\School\\CHF\\chf\\test_dmp\\homepage\\templates/base.htm", "uri": "base.htm", "source_encoding": "ascii", "line_map": {"68": 85, "74": 68, "16": 4, "18": 0, "28": 2, "29": 4, "30": 5, "34": 5, "35": 16, "36": 20, "37": 20, "38": 22, "39": 22, "40": 32, "41": 32, "42": 32, "43": 49, "44": 50, "45": 53, "46": 54, "47": 57, "48": 75, "49": 76, "50": 80, "55": 97, "56": 104, "62": 85}}
__M_END_METADATA
"""
