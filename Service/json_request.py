"""
Return a JSON Object containing the list of firms
@author Sebastian Ampuero
@date 8.12.2017
"""
import json
from Entities.Ansprechpartner import Ansprechpartner
from Service.firmen_service import get_firm_by_name


# Retrieve a firm as json format by name
# @return the firm in json format, if not found null is returned
def get_firm_json(name):
    firmas = get_firm_by_name(name)
    dict_list = []
    if len(firmas) != 0:
        for a_firma in firmas:
            dict_list.append(a_firma.json())
        return json.dumps(dict_list)
    else:
        return "{}"


# Retrive a list of titles in json format
# @return a list of titles in json format
def get_title(title):
    titles = Ansprechpartner.title_list
    titles_list = []
    for a_title in titles:
        if title in a_title.lower():
            title_dict = {'titel': a_title}
            titles_list.append(title_dict)
    if len(titles_list) == 0:
        return "{}"
    return json.dumps(titles_list)
