from tokens import *


class Parser():
    def __init__(self, tokens):
        # The stack of tokens generated by the lexer
        self.tokens = tokens

    def raise_error(self, token):
        raise Exception("Ohnoes, an error occurred at position {}.".format(token.loc))

    # See if the next token has the correct type
    def eat(self, type_token):
        token = self.peek()
        if token.type == type_token:
            self.next()
        else:
            self.raise_error(token)

    # Token must match at least one of the types
    def eat_any(self, type_tokens):
        token = self.peek()
        containsType = False
        for type_token in type_tokens:
            if token.type == type_token:
                containsType = True
                break
        if containsType:
            self.next()
        else:
            self.raise_error(token)

    # Pops a token from the stack (from the end of the list)
    def next(self):
        return self.tokens.pop()

    # Inserts token back into the stack (at the end of the list)
    def push(self, token):
        self.tokens.append(token)

    # Gets the next token, then pushes the token back and finally returns the token
    def peek(self):
        token = self.tokens.pop()
        self.push(token)
        return token

    # Peek a specific number of Tokens
    # Put them back in the order that they came from
    def peek_many(self, n):
        tokens1 = []
        for x in range(0, n):
            token = self.next()
            tokens1.append(token)

        for tok in reversed(tokens1):
            self.push(tok)
        return tokens

    def parse(self):
        left = int(self.next().value)

        self.eat(Special.NewLine)
        op = self.peek()
        self.eat_any([Operator.plus, Operator.sub,
                       Operator.mult, Operator.div])

        self.eat(Special.Whitespace)  # Whitespaces can also be parsed
        right = int(self.next().value)
        if op.type == Operator.plus:
            print(left + right)
        elif op.type == Operator.sub:
            print(left - right)
        elif op.type == Operator.mult:
            print(left * right)
        else:
            print(left / right)