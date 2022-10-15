# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1647033398.1448307
_enable_loop = True
_template_filename = 'res/templates/supp_etudiantByName.html'
_template_uri = 'supp_etudiantByName.html'
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
        message = context.get('message', UNDEFINED)
        type = context.get('type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h3>Suppression d\'un étudiant</h3>\r\n<pre>\r\nSuppression de données contenues dans la base.\r\n2 types de suppression disponibles : à l\'aide du numéro ou à l\'aide de "nom" + "prénom".\r\n</pre>\r\n\r\n<h3>Suppression d\'un étudiant par nom et prénom</h3>\r\n\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n <form action="suppressByName" method="POST">\r\n  <div class="form-group">\r\n    <label for="Prénom">Prénom:</label>\r\n    <input type="text" class="form-control" placeholder="Prénom de l\'étudiant" name="prenom" id="prenom">\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="Nom">Nom:</label>\r\n    <input type="text" class="form-control" placeholder="Nom de l\'étudiant" name="nom" id="nom">\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Supprimer</button>\r\n</form> ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/supp_etudiantByName.html", "uri": "supp_etudiantByName.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 10, "36": 10, "37": 10, "38": 10, "44": 38}}
__M_END_METADATA
"""
