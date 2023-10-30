import logging
from docx import Document
import marysa, kategorie, generator, module_importer

logging.basicConfig(filename='log.txt', level=logging.DEBUG)
with open('log.txt', 'w'):
    pass


#subject = 'marysa'

def callfunc(subject):
    category_list = ['temamotiv', 'casoprostor', 'kompozice', 'druhzanr', 'lyrickysubjekt', 'postava', 'zpusoby', 'promluvy']
    specific_categories = []
    global_categories = [] 
    temp = """"""

    for i in range(len(category_list)):
        temp = module_importer.module_import_func(subject, category_list[i])
        specific_categories.append(temp)

    for i in range(len(category_list)):
        temp = getattr(kategorie, category_list[i])
        global_categories.append(temp)

    finish = []

    for i in range(len(specific_categories)):
        temp = generator.rewrite_text(global_categories[i], generator.initial_system_prompt, specific_categories[i])
        finish.append(temp)

    return finish
