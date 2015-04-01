# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425666583.635708
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp/homepage/templates/index.html'
_template_uri = 'homepage/templates/index.html/'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<title>Homepage</title>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer("\r\n\r\n<h1>The Colonial Heritage Foundation</h1>\r\n<p>The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America's founding. To accomplish this mission, the Foundation engages in a broad array of activities. Among these are the development and presentation of educational exhibits, the coordination of reading and discussion groups to encourage the study of America's historical writings, the presentation of lectures and seminars regarding America's founding era, the coordination of historical reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the occupational skills of early America.</p>\r\n<br><h3>Education Exhibits</h3>\r\n<p>At its heart, the Foundation is an educational institution. One of its major undertakings is developing exhibits and programs that can help bring to life the history surrounding America's colonial period and is founding generation.  To this end, the Foundation has developed a variety of traveling exhibits.  One exhibit is focuses on the importance of the press in the American Revolution and of the continued importance of a free press in America today.  The central artifact of this exhibit is a replica of the Isaiah Thomas Press, an 18th century press that was influential building support for American independence. Another exhibit focuses on the early colonial period and the ides of self-government that were planted in Jamestowne and Plimoth.  At the center of this exhibit is a scale model of the Mayflower. The exhibit also includes replicas of various artifacts from the early colonial period.</p>\r\n<br><h3>Reading and Discussion Groups</h3>\r\n<p>The Foundation coordinates and helps to establish community groups to encourage the reading and discussion of America's historical documents. For example, the Federalist Papers and the Anti-federalist Papers were publications that made the argument for and against the adoption of America's current constitution. The study and discussion of these documents can help Americans today understand the issues that were of most concern to our founding generation regarding the establishment of a strong federal government. These documents were written in a language style that is foreign to most contemporary readers. By providing recommended reading schedules, discussion questions, and materials to help modern readers read and grasp federal-period writings, the Foundation hopes to encourage small, community-based groups to undertake independent study of such founding documents. These discussion groups will be conducted year-round by volunteers and held in homes or community meeting places throughout the nation. </p>\r\n<br><h3>Workshops, Lectures, and Seminars</h3>\r\n<p>The Foundation sponsors lectures, seminars and workshops about the values, culture, skills, and history of America's founding era. Such events may be coordinated with universities and other educationally-focused organizations to educate adults about the sacrifices that early Americans made to provide today's population with the freedoms we enjoy. These events  seek to inspire individuals to engage in community-based educational activities to increase exposure an awareness of the history surrounding America's founding. Lectures, seminars and workshops are coordinated and presented year-round by Foundation volunteers. Depending on the venue, they are offered either free of charge or for a fee. </p>\r\n<br><h3>Historical Reenactment</h3>\r\n<p>The Foundation sponsors the Colonial Heritage Festival, the largest colonial living and reenactment event west of the Mississippi River. This event is located in Orem, Utah as is attended by more than 40,000 people annually. The Foundation also coordinates presentations of individual reenactors portraying notable figures from the American founding such as  George Washington, Benjamin Franklin, and others.</p>\r\n<br><h3>Apprenticeships</h3>\r\n<p>The Foundation seeks to help individuals who have developed skills peculiar to America's founding era to pass those skills on to others. One way to preserve these skills is to teach them to younger individuals. The Foundation seeks to match skilled artisans and craftsmen with eager young individuals for the purposing of learning trade and artistic skills. </p>\r\n<br><h3>Internships</h3>\r\n<p>In conjunction with its educational exhibits, the Foundation offers unpaid internships intended for students studying Museum Studies or History Education.  Individuals selected for the program spend one to three months accompanying educational exhibits to schools, teaching students about Colonial American History and portraying notable figures from the period.  </p>\r\n\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "homepage/templates/index.html/", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\test_dmp/homepage/templates/index.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 5, "50": 5}}
__M_END_METADATA
"""
