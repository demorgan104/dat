import os
import re
import shutil


def generate_conanfile(dst, config):
    # Create the extensions folder
    package_path = config['package_path']
    extensions_dir = os.path.join(package_path, 'extensions')
    extensions_dst = os.path.join(dst, 'extensions')
    if os.path.exists(extensions_dir):
        shutil.copytree(
            extensions_dir,
            extensions_dst
        )
    else:
        extensions_dir_local = os.path.join(os.path.dirname(__file__), 'extensions')
        shutil.copytree(
            extensions_dir_local,
            extensions_dst
        )
    requirements = ""
    if 'depends' in config:
        for package_name, version_entry in config['depends'].items():
            package = "{package_name}/{version}@stable/release".format(
                package_name = package_name,
                version = str(version_entry['version'])
            )
            requirements += "\"{package}\",".format(
                package = package
            )
        requirements = requirements[:-1] # remove the last , 
    else:
        requirements = "\"\""

    replacements = {
        'name': config['name'],
        'description': config['description'],
        'url': config['url'],
        'version': config['version'],
        'requirements': requirements
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

