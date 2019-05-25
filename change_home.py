#! /usr/bin/env python3

import shutil

def get_dirnames():
    """
    Function:
            get_dirnames( )
    Description:
            Retrieve the default directory names under /home.
    Arguments:
            None
    Returns:
            A list of strings containing directory names.
    """
    return [ "Music",
             "Downloads",
             "Templates",
             "Pictures",
             "Videos",
             "Public",
             "Documents" ]

def move_dirs():
    """
    Function:
            move_dirs( )
    Description:
            Rename the directories under /home with lower case.
    Arguments:
            None
    Returns:
            None
    """
    dirnames = get_dirnames()
    for d in dirnames:
        shutil.move(d, d.lower())


def get_user_config():
    """
    Function:
            get_user_config( )
    Description:
            Get the location of the configuration file.
    Arguments:
            None
    Returns:
            A string with the location of the user-dirs configuration.
    """
    return ".config/user-dirs.dirs"

def change_config():
    """
    Function:
            change_config( )
    Description:
            Change the home directory configuration to reflect lowercase names.
    Arguments:
            None
    Returns:
            None
    """
    user_config = get_user_config()
    dirnames = get_dirnames()

    with open(user_config, 'r') as f:
        conf = f.read()
        for d in dirnames:
            conf.replace(d, d.lower())

    with open(user_config, 'w') as f:
        f.write(conf)


def main():
    """
    Function:
            main( )
    Description:
            Move directories to lowercase names and change configuration.
    Arguments:
            None
    Returns:
            None
    """
    # Move directories
    move_dirs()

    # Change config
    change_config()

if __name__ == "__main__":
    main()
