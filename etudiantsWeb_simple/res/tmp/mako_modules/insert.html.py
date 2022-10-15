# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1647026057.8848808
_enable_loop = True
_template_filename = 'res/templates/insert.html'
_template_uri = 'insert.html'
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
        __M_writer('\r\n\r\n<h3>Insertion d\'un étudiant</h3>\r\n\r\n<pre>\r\nInsertion de données dans la base.\r\n</pre>\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n <form action="insertDone" method="POST" class="needs-validation" novalidate>\r\n  <div class="form-group">\r\n    <label for="prenom">Prénom:</label>\r\n    <input type="text" class="form-control" id="prenom" placeholder="Entrer le prénom" name="prenom" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="nom">Nom:</label>\r\n    <input type="text" class="form-control" id="nom" placeholder="Enter le nom" name="nom" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label class="form">\r\n    <label for="bday">Date de naissance de l\'étudiant :</label>\r\n    <input type="date" class="form-control" id="bday" placeholder="Date de naissance de l\'étudiant" name="bday" required>\r\n    </label>\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Insérer</button>\r\n</form>\r\n\r\n<script>\r\n// Disable form submissions if there are invalid fields\r\n(function() {\r\n  \'use strict\';\r\n  window.addEventListener(\'load\', function() {\r\n    // Get the forms we want to add validation styles to\r\n    var forms = document.getElementsByClassName(\'needs-validation\');\r\n    // Loop over them and prevent submission\r\n    var validation = Array.prototype.filter.call(forms, function(form) {\r\n      form.addEventListener(\'submit\', function(event) {\r\n        if (form.checkValidity() === false) {\r\n          event.preventDefault();\r\n          event.stopPropagation();\r\n        }\r\n        form.classList.add(\'was-validated\');\r\n      }, false);\r\n    });\r\n  }, false);\r\n})();\r\n</script> ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/insert.html", "uri": "insert.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 8, "36": 8, "37": 8, "38": 8, "44": 38}}
__M_END_METADATA
"""
