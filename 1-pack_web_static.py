#!/usr/bin/python3
"""Script that generates a .tgz archive from the contents of the web_static."""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to generate a .tgz archive."""
    # Create the folder versions if not exists
    local("mkdir -p versions")
    # Get the current date and time in the format YYYYMMDDHHMMSS
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    # Create the name of the file
    # The file name has the format: web_static_YYYYMMDDHHMMSS.tgz
    file = "versions/web_static_{}.tgz".format(current_date)
    try:
        # Compress the files
        local("tar -cvzf {} web_static".format(file))
        # If the file was created
        return file
    except Exception as execption:
        # If the file doesn't be created return None
        return None
