class Expr:
    def pretty(self, indent=0):
        raise NotImplementedError()

class Var(Expr):
    def __init__(self, name):
        self.name = name

    def pretty(self, indent=0):
        return '  ' * indent + f'Var({self.name})'

class Not(Expr):
    def __init__(self, expr):
        self.expr = expr

    def pretty(self, indent=0):
        return '  ' * indent + 'Not\n' + self.expr.pretty(indent + 1)

class And(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def pretty(self, indent=0):
        return '  ' * indent + 'And\n' + self.left.pretty(indent + 1) + '\n' + self.right.pretty(indent + 1)

class Or(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def pretty(self, indent=0):
        return '  ' * indent + 'Or\n' + self.left.pretty(indent + 1) + '\n' + self.right.pretty(indent + 1)

class Implies(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def pretty(self, indent=0):
        return '  ' * indent + 'Implies\n' + self.left.pretty(indent + 1) + '\n' + self.right.pretty(indent + 1)

class Iff(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def pretty(self, indent=0):
        return '  ' * indent + 'Iff\n' + self.left.pretty(indent + 1) + '\n' + self.right.pretty(indent + 1)
