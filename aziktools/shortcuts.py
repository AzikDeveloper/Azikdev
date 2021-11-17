from aziktools.template_conf.main import env
from aziktools.db.models import *

""" if there is a QuerySet in context, this function turns it into a python dictionary type so that 
jinja2 can understand it
"""
def queryset_handler(value: QuerySet):
    object_dict_list = []
    for _instance in value.instances:
        object_dict = {}
        for field in _instance.fields:
            object_dict[field] = getattr(_instance, field)
        object_dict_list.append(object_dict)
    return object_dict_list


""" this function takes html template file name and context and process it. After that passes it to the jinja2 
    environment to return plain text. 
"""
def render(template_name, context=None):
    if context is None:
        context = {}

    template = env.get_template(template_name)
    for key, value in context.items():
        if type(value).__name__ == 'QuerySet':
            context[key] = queryset_handler(value)
    return template.render(**context)
