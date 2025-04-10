import re

def tokenize(string):
    """
    This function takes in a string and splits it into tokens.

    For example this string:
    "(p & q) -> !(r | s)"
    Gets split into these tokens:
    "(", "p", "&", "q", ")", "->", "!", "(", "r", "|", "s", ")"

    string : the input string to be tokenized.
    """
    token_spec = [
        ('LPAREN',  r'\('),
        ('RPAREN',  r'\)'),
        ('IFF',     r'<->'),
        ('IMPLIES', r'->'),
        ('AND',     r'&'),
        ('OR',      r'\|'),
        ('NOT',     r'!'),
        ('VAR',     r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('SKIP',    r'[ \t]+'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_spec)
    for mo in re.finditer(tok_regex, string):
        kind = mo.lastgroup
        value = mo.group()
        if kind != 'SKIP':
            yield (kind, value)
    yield ('EOF', '')
