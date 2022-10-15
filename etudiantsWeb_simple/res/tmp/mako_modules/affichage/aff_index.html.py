# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1587764568.0711274
_enable_loop = True
_template_filename = 'res2020/templates/affichage/aff_index.html'
_template_uri = 'affichage/aff_index.html'
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
        params = context.get('params', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n<h3 class="center">Affichage</h3>\r\n\r\n<pre>\r\nAffichage des données contenues dans la base SQLite.\r\n4 affichages disponibles : tout afficher, affichage par âge, affichage du plus jeune, afficher avec Id.\r\n</pre>\r\n\r\n')

        mesEtud = []
        for id, prenom, nom, dt in params['liste_etudiants']:
                d = dt.split('-')
                sd = d[2]+"/"+ d[1]+"/"+d[0]
                s ="{:10s} {:10s} né(e) le {}".format(prenom, nom, sd)
                mesEtud.append(s)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['id','nom','prenom','mesEtud','sd','d','dt','s'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<h3>Liste des étudiants</h3>\r\n\r\n')
        for e in mesEtud :
            __M_writer('\t')
            __M_writer(str(e))
            __M_writer(' <br/>\r\n')
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res2020/templates/affichage/aff_index.html", "uri": "affichage/aff_index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 2, "35": 10, "36": 11, "37": 12, "38": 13, "39": 14, "40": 15, "41": 16, "42": 17, "43": 18, "46": 17, "47": 21, "48": 22, "49": 22, "50": 22, "51": 24, "57": 51}}
__M_END_METADATA
"""
