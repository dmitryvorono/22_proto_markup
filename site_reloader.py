import os
from livereload import Server
from jinja2 import Environment, FileSystemLoader


def load_jinja_templates(templates_folder):
    jinja_env = Environment(loader=FileSystemLoader(templates_folder),
                            trim_blocks=True,
                            lstrip_blocks=True)
    jinja_env
    with os.scandir(templates_folder) as folder_iterator:
        return {entry.name: jinja_env.get_template(entry.name)
                for entry in folder_iterator if entry.is_file()}


def render_index_page(jinja_template, output):
    with open(output, 'w') as file_handler:
        file_handler.write(jinja_template.render())


def make_site():
    templates_folder = 'templates'
    jinja_templates = load_jinja_templates(templates_folder)
    render_index_page(jinja_templates['index.html'], 'index.html')
    render_index_page(jinja_templates['requests.html'], 'requests.html')


if __name__ == '__main__':
    server = Server()
    server.watch('templates/*.html', make_site)
    server.watch('css/*.css', make_site)
    server.serve(root='.')
