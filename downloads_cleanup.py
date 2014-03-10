import os
import shutil

DOWNLOADS_PATH = os.path.expanduser( '~' ) + "//Downloads"

def organize_downloads():
    files = get_files()
    files = get_extensions( files )
    make_folders( files )
    pass

def get_files():
    return( os.listdir( DOWNLOADS_PATH ) )

def get_extensions( fils ):
    files = {}
    for fil in fils:
        name, extension = os.path.splitext( fil )
        if extension not in files:
            files[extension] = []

        files[extension].append( fil )

    return files

def make_folders( files ):
    for extension in files.keys():
        temp_path = DOWNLOADS_PATH + "//" + extension[1:]
        if not os.path.exists( temp_path ):
            os.mkdir( temp_path )
        file_names = files[extension]
        for fil in file_names:
            src_path = DOWNLOADS_PATH + '//' + fil
            if not os.path.isdir( src_path ) and fil[0] != '.':
                print 'Copying {0} to {1}'.format( src_path, temp_path )
                shutil.copy( src_path, temp_path )
                print 'Removing {0}'.format( src_path )
                os.remove( src_path )
