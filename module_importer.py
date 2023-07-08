import logging
import marysa, kategorie, generator

def module_import_func(module_name, litcategory):
    try:
        module = __import__(module_name)        
        if hasattr(module, litcategory):
            return(getattr(module, litcategory))
        else:
            error_msg = f"No variable named {litcategory} in module {module_name}"
            logging.error(error_msg)        
    except ImportError:
        error_msg = f"No module named {module_name} found"
        logging.error(error_msg)
