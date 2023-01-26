def delete_file(path):
    """Funcion que borra un archivo dado un path"""
    """Funcion que borra un archivo dado un path"""
    import os
    if os.path.isfile(path):
        os.remove(path)
    else:  ## Show an error ##
        print("Error: %s file not found" % path)