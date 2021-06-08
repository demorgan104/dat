"""
    A module that helps with template replacements
"""

import re


def replace_and_create(replacements, template, dst):
    """
    TBD
    """

    pattern = re.compile(r"<\$(.*)>")
    with open(template, "r") as template_file:
        with open(dst, "w") as new_file:
            for line in template_file:
                match = re.search(pattern, line)
                new_line = line
                if match:
                    token = match.group(1)
                    new_line = line.replace(
                        "<${token}>".format(token=token), str(replacements[token])
                    )
                new_file.write(new_line)
