from tokenizer import tokenize
from parser import Parser

def parse_expr(input_str):
    tokens = tokenize(input_str)
    parser = Parser(tokens)
    return parser.parse()

if __name__ == "__main__":
    test = "(p & q) -> !(r | s)"
    ast = parse_expr(test)
    print(ast.pretty())
