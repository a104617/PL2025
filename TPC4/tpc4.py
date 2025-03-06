import ply.lex as lex

tokens = (
    'SELECT',
    'WHERE',
    'LIMIT',
    'VARIABLE',
    'RESOURCE',
    'STRING',
    'LPAREN',
    'RPAREN',
    'DOT',
    'COLON',
    'AT',
    'EQUALS',
    'COMMA',
    'NUMBER',
)

t_LPAREN = r'\{'
t_RPAREN = r'\}'
t_DOT = r'\.'
t_COLON = r':'
t_AT = r'@'
t_EQUALS = r'='
t_COMMA = r','
t_ignore = ' \t'

def t_SELECT(t):
    r'select'
    return t

def t_WHERE(t):
    r'where'
    return t

def t_LIMIT(t):
    r'LIMIT'
    return t

def t_VARIABLE(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_RESOURCE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'"[^"]*"@[a-z]+'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



lexer = lex.lex()

data = """
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en.
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
"""

lexer.input(data)

for tok in lexer:
    print(tok)

