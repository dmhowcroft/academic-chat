import ply.lex as lex
import ply.yacc as yacc

# List of tokens
reserved = {
    'general'       :'GENERAL',
    'professional'  :'PROFESSIONAL',
    'interests'     :'INTERESTS',

    'last_pubs'     :'LAST_PUBS',
    'pubs_between'  :'PUBS_BETWEEN',
    'pubs_with'     :'PUBS_WITH',
    'pubs_venue'    :'PUBS_VENUE',

    'proj_title'    :'PROJ_TITLE',
    'proj_desc'     :'PROJ_DESC',
    'proj_repo'     :'PROJ_REPO',

    'blog_last'     :'BLOG_LAST',
    'blog_titles'   :'BLOG_TITLES',
    'blog_post'     :'BLOG_POST',
    'blog_random'   :'BLOG_RANDOM'
}
tokens = ['NUMBER', 'TEXT', 'QUOT', 'ID'] + list(reserved.values())

# Simple tokens
t_QUOT = r'["\']'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if reserved.get(t.value) is not None:
        t.type = reserved.get(t.value)    # Check for reserved words
        t.value = t.value
    else:
        t.type = 'TEXT'
        t.value = str(t.value)
    return t

# Complex tokens
# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Not an integer %d", t.value)
        t.value = 0
    return t

def t_TEXT(t):
    r'[a-zA-Z_ ][a-zA-Z0-9_ ]*'
    t.value = str(t.value)
    return t


# Build the lexer
lexer = lex.lex()

def p_root(t):
    '''exp : about
           | pubs
           | projects
           | blog'''
    t[0] = t[1]

def p_about(t):
    '''about : GENERAL
             | PROFESSIONAL
             | INTERESTS'''
    t[0] = t[1]

def p_pubs(t):
    '''pubs : LAST_PUBS NUMBER
            | PUBS_BETWEEN NUMBER NUMBER
            | PUBS_WITH QUOT TEXT QUOT
            | PUBS_VENUE QUOT TEXT QUOT'''
    if t[1] == 'last_pubs':
        t[0] = "{} '{}'".format(t[1], t[2])
    elif t[1] == 'pubs_between':
        t[0] = "{} {} {}".format(t[1], t[2], t[3])
    else:
        t[0] = "{} '{}'".format(t[1], t[3])

def p_projects(t):
    '''projects : PROJ_TITLE QUOT TEXT QUOT
                | PROJ_DESC QUOT TEXT QUOT
                | PROJ_REPO QUOT TEXT QUOT'''
    t[0] = "{} '{}'".format(t[1], t[3])

def p_blog(t):
    '''blog : BLOG_LAST
            | BLOG_TITLES NUMBER
            | BLOG_POST QUOT TEXT QUOT
            | BLOG_RANDOM'''
    if t[1] == 'blog_last' or t[1] == 'blog_random':
        t[0] = t[1]
    elif t[1] == 'blog_titles':
        t[0] = "{} {}".format(t[1], t[2])
    elif t[1] == 'blog_post':
        t[0] = "{} '{}'".format(t[1], t[3])

def p_error(t):
    print("I'm sorry, I don't understand that: {}".format(t))

parser = yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            s = input('calc > ')   # Use raw_input on Python 2
        except EOFError:
            break
        print(parser.parse(s))