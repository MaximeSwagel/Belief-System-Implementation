from ast_nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def advance(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def parse(self):
        return self.parse_iff()

    def parse_iff(self):
        expr = self.parse_implies()
        while self.peek()[0] == 'IFF':
            self.advance()
            right = self.parse_implies()
            expr = Iff(expr, right)
        return expr

    def parse_implies(self):
        expr = self.parse_or()
        while self.peek()[0] == 'IMPLIES':
            self.advance()
            right = self.parse_or()
            expr = Implies(expr, right)
        return expr

    def parse_or(self):
        expr = self.parse_and()
        while self.peek()[0] == 'OR':
            self.advance()
            right = self.parse_and()
            expr = Or(expr, right)
        return expr

    def parse_and(self):
        expr = self.parse_not()
        while self.peek()[0] == 'AND':
            self.advance()
            right = self.parse_not()
            expr = And(expr, right)
        return expr

    def parse_not(self):
        if self.peek()[0] == 'NOT':
            self.advance()
            return Not(self.parse_not())
        else:
            return self.parse_atom()

    def parse_atom(self):
        tok_type, tok_val = self.peek()
        if tok_type == 'LPAREN':
            self.advance()
            expr = self.parse()
            if self.advance()[0] != 'RPAREN':
                raise SyntaxError("Expected ')'")
            return expr
        elif tok_type == 'VAR':
            self.advance()
            return Var(tok_val)
        else:
            raise SyntaxError(f"Unexpected token: {tok_type}")
