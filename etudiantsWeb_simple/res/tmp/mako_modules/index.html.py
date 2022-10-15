# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1647023865.1765344
_enable_loop = True
_template_filename = 'res/templates/index.html'
_template_uri = 'index.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n<h3 class="center">Rappel du sujet :</h3>\r\n\r\n<h4>\r\n"Réaliser une jolie interface web pour afficher la base, insérer et supprimer des étudiants".\r\n</h4>\r\n\r\n\r\n<pre class="bg-info text-white">\r\n<b>Remarques :</b>\r\n- Utilisation de Cherrypy.\r\n- Ajout de ressources statiques (fichiers css et javascript).\r\n- Utilisation de Mako pour les templates.\r\n- Utilisation de quelques élements de Bootstrap pour que ce soit plus joli.\r\n\r\n- Implémentation d\'une base "étudiants".\r\n- 4 affichages disponibles (tout, plus jeune, par âge, avec Id).\r\n- 2 suppression disponibles (par id, par nom et prénom).\r\n- 1 insertion disponible.\r\n</pre>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 23, "40": 34}}
__M_END_METADATA
"""
