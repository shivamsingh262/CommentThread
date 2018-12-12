import mongoengine
import os
from jinja2 import Environment, FileSystemLoader

path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = ROOT[:ROOT.rindex('/')]
MEDIA_ROOT = path(ROOT, 'static/')
TEMPLATE_ROOT = path(ROOT, 'templates/')
env = Environment(loader=FileSystemLoader(TEMPLATE_ROOT))

main_template = env.get_template("main.html")

mongoengine.connect('commenter', connect=False)

