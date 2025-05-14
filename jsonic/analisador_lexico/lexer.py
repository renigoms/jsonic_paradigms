import ply.lex as lex

tokens = [
    "OPEN_JSON",
    "WRITE_JSON",
    "SELECT_JSON",
    "SAVE_JSON",
    "INTO",
    "TARGET_PATH",
    "PATH_JSON",
    "KEY",
    "EQUAL",
    "TEXT",
    "ALL",
    "DATA_JSON",
    "CLOSE_JSON"
]

t_ALL = r'\*'
t_OPEN_JSON = r'OPEN_JSON|open_json'
t_WRITE_JSON = r'WRITE_JSON | write_json'
t_SAVE_JSON = r'SAVE_JSON | save_json'
t_SELECT_JSON = r'SELECT_JSON | select_json'
t_KEY = r'KEY | key'
t_INTO = r'INTO | into'
t_EQUAL = r'\='
t_CLOSE_JSON = r'CLOSE_JSON | close_json'

def t_TEXT(t):
    r'"[a-zçA-ZÇ_]+[a-zçA-ZÇ0-9_]+"'
    return t


def t_PATH_JSON(t):
    r'"[a-zA-Z_]*[a-zA-Z0-9_]*\.json"'
    return t

def t_TARGET_PATH(t):
    r'"([a-zA-Z]:\/(?:[\w\-]+\/)*[\w\-]*|\/(?:[\w\-]+\/)*[\w\-]*)"'
    return t

def t_DATA_JSON(t):
    r'"\{(?:\s*"[a-zA-Z0-9_]+"s*:\s*"?[^"]*"?,?)*\}"'
    return t
# SPACE IGNORE
t_ignore = "\t' '"

# ERROR HANDLING FOR UNRECOGNIZED CHARACTERS
def t_error(t):
    print(f"Illegal Character '{t.value[0]}'")
    t.lexer.skip(1)


# CONFIGURING TOKENS
lexer = lex.lex()

def get_lexer():
    return lexer

"""
Lang commands

OPEN_JSON "test.json"
SAVE_JSON "test.json" INTO "c:/user/renan"
WRITE_JSON "{"teste":"test"}" INTO "c:/user/renan"
SELECT_JSON KEY = "TEST" OR SELECT_JSON *
CLOSE_JSON
"""