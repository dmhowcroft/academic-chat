from nltk.tokenize import word_tokenize as tkz

def params_as_integer(params):
    return (int(params[0]),)

def params_as_integers(params):
    return int(params[0]), int(params[1])

def params_as_string(params):
    p1 = str(params[0])
    return [p1]

dict_function = {
    'general': lambda p: [],
    'professional': lambda p: [],
    'interests' : lambda p: [],

    'last_pubs': lambda p: params_as_integer,
    'pubs_between'  :params_as_integers,
    'pubs_with'     :params_as_string,
    'pubs_venue'    :params_as_string,

    'proj_title'    :params_as_string,
    'proj_desc'     :params_as_string,
    'proj_repo'     :params_as_string,

    'blog_last'     :lambda p:[],
    'blog_titles'   :params_as_integer,
    'blog_post'     :params_as_string,
    'blog_random'   :lambda p:[],
}

def read_input(raw) :
    p = tkz(raw)
    hd, tl = p[0], p[1:]
    tl = dict_function[hd](tl)
    return [hd] + tl
