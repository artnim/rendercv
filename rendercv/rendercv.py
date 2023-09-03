from jinja2 import Environment, FileSystemLoader

from data.content import CurriculumVitae
# from . import tinytex # https://github.com/praw-dev/praw/blob/master/praw/reddit.py
# from . import templates, sonra mesela: classic.render() tarzi seyler olabilir
from tinytex.render import render

import os
import json



if __name__ == "__main__":
    workspace = os.path.dirname(os.path.dirname(__file__))
    templateName = "classic"
    templatePath = os.path.join(workspace, "rendercv", "templates", templateName)
    environment = Environment(loader=FileSystemLoader(templatePath))
    environment.block_start_string = "((*"
    environment.block_end_string = "*))"
    environment.variable_start_string = "((("
    environment.variable_end_string = ")))"
    environment.comment_start_string = "((="
    environment.comment_end_string = "=))"

    template = environment.get_template(f"{templateName}.tex.j2")

    input_file_path = os.path.join(workspace, "tests", "inputs", "test.json")
    with open(input_file_path) as file:
        raw_json = json.load(file)

    cv = CurriculumVitae(**raw_json)

    output_latex_file = template.render(cv=cv)

    # Create an output file and write the rendered LaTeX code to it:
    output_file_path = os.path.join(workspace, "tests", "outputs", "test.tex")
    with open(output_file_path, "w") as file:
        file.write(output_latex_file)

    render(output_file_path)

    

        