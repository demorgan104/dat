"""
    DAT Logger module
"""

import logging

# create logger
app_logger = logging.getLogger("dat")
app_logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(levelname)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
app_logger.addHandler(ch)
