import os
import re


def generate_conanfile(dst, config):
    replacements = {
        'name': config['name'],
        'description': config['description'],
        'url': config['url'],
        'version': config['version']
    }
    new_conan_file = os.path.join(
        dst,
        'conanfile.py'
    )
    conan_file_template = os.path.join(
        os.path.dirname(__file__),
        'conanfile_template'
    )
    pattern = re.compile(
        r"<\$(.*)>"
    )
    with open(conan_file_template, 'r') as conan_template:
        with open(new_conan_file, 'w') as new_conan_recipe:
            for line in conan_template:
                match = re.search(pattern, line)
                new_line = line
                if match:
                    token = match.group(1)
                    new_line = line.replace(
                        '<${token}>'.format(
                            token=token
                        ), str(replacements[token])
                    )
                new_conan_recipe.write(new_line)
    return new_conan_file

