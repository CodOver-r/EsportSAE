# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1649444103.336969
_enable_loop = True
_template_filename = 'res/templates/aff_parAge.html'
_template_uri = 'aff_parAge.html'
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
        mesEtud = context.get('mesEtud', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n\r\n<h3>Liste des étudiants, classés par ordre d'âge</h3>\r\n\t")
        # code python pour changer l'affichage de la date!!!
        from BDEtudiantUtils import isoDate2String
        maListe = []
        for id ,p, n, d in mesEtud :
            maListe.append((p,n,isoDate2String(str(d))))        
                
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['id','maListe','d','n','isoDate2String','p'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\t\r\n')
        for p, n, d in maListe :
            __M_writer('\t')
            __M_writer(str(d))
            __M_writer(' : ')
            __M_writer(str(p))
            __M_writer(' ')
            __M_writer(str(n))
            __M_writer(' <br/>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/aff_parAge.html", "uri": "aff_parAge.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 4, "36": 5, "37": 6, "38": 7, "39": 8, "40": 9, "41": 10, "44": 9, "45": 10, "46": 11, "47": 11, "48": 11, "49": 11, "50": 11, "51": 11, "52": 11, "58": 52}}
__M_END_METADATA
"""
