class Expr:
    def pretty(self, indent=0):
        raise NotImplementedError()

class Var(Expr):
    def __init__(self, name):
        self.name = name

    def pretty(self, indent=0):
        return '  ' * indent + f'Var({self.name})'

    # Added for string-based revision logic
    def __str__(self):
        return self.name

class Not(Expr):
    def __init__(self, expr):
        self.expr = expr

    def pretty(self, indent=0):
        return '  ' * indent + 'Not\n' + self.expr.pretty(indent + 1)

    # Added for string-based revision logic
    def __str__(self):
        return f"!({self.expr})"

class And(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def pretty(self, indent=0):
        return '  ' * indent + 'And\n' + self.left.pretty(indent + 1) + '\n' + self.right.pretty(indent + 1)

    # Added for string-based revision logic
    def __str__(self):
        return f"({self.left} & {self.right})"

class Or(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def pretty(self, indent=0):
        return '  ' * indent + 'Or\n' + self.left.pretty(indent + 1) + '\n' + self.right.pretty(indent + 1)

    # Added for string-based revision logic
    def __str__(self):
        return f"({self.left} | {self.right})"

class Implies(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def pretty(self, indent=0):
        return '  ' * indent + 'Implies\n' + self.left.pretty(indent + 1) + '\n' + self.right.pretty(indent + 1)

    # Added for string-based revision logic
    def __str__(self):
        return f"({self.left} -> {self.right})"

class Iff(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def pretty(self, indent=0):
        return '  ' * indent + 'Iff\n' + self.left.pretty(indent + 1) + '\n' + self.right.pretty(indent + 1)

    # Added for string-based revision logic
    def __str__(self):
        return f"({self.left} <-> {self.right})"
