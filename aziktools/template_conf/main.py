# jinja2 integration. env is an environment to work with html templates

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)