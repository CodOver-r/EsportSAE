# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1647032798.2980492
_enable_loop = True
_template_filename = 'res/templates/aff_plusJeune.html'
_template_uri = 'aff_plusJeune.html'
_source_encoding = 'utf-8'
_exports = []


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
    return runtime._inherit_from(context, 'template.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        monEtud = context.get('monEtud', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3>Le ou la plus jeune!!! :</h3>\r\n\r\n')
        __M_writer(str(monEtud))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/aff_plusJeune.html", "uri": "aff_plusJeune.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 5, "35": 5, "41": 35}}
__M_END_METADATA
"""
