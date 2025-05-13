class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0

    def current_token(self):
        if self.current_index < len(self.tokens):
            return self.tokens[self.current_index]
        return None

    def advance(self):
        if self.current_index < len(self.tokens):
            self.current_index += 1

    def expect(self, expected_type):
        token = self.current_token()
        if token and token[0] == expected_type:
            self.advance()
        else:
            raise SyntaxError(
                f"Se esperaba {expected_type}, pero se encontró {token}")

    def parse(self):
        try:
            self.program()
            print("El programa es válido.")
        except SyntaxError as e:
            print(f"Error de sintaxis: {e}")

    def program(self):
        while self.current_token():
            self.statement()
            self.expect('SEMICOLON_SPEC')

    def statement(self):
        token = self.current_token()
        if token[0] in ['ENTERO', 'FLOTANTE', 'STRING']:
            self.declaration()
        elif token[0] == 'IDENTIFIER':
            self.assignment()
        elif token[0] == 'IF':
            self.if_statement()
        elif token[0] == 'WHILE':
            self.while_statement()
        else:
            raise SyntaxError(f"Declaración no válida: {token}")

    def declaration(self):
        self.advance()
        self.expect('IDENTIFIER')
        if self.current_token() and self.current_token()[0] == 'ASSIGN_OP':
            self.advance()
            self.expression()

    def assignment(self):
        self.expect('IDENTIFIER')
        self.expect('ASSIGN_OP')
        self.expression()

    def if_statement(self):
        self.advance()
        self.expect('LPAREN_SPEC')
        self.expression()
        self.expect('RPAREN_SPEC')
        self.block()
        if self.current_token() and self.current_token()[0] == 'ELSE':
            self.advance()
            self.block()

    def while_statement(self):
        self.advance()
        self.expect('LPAREN_SPEC')
        self.expression()
        self.expect('RPAREN_SPEC')
        self.block()

    def expression(self):
        self.term()
        while self.current_token() and self.current_token()[0] in ['PLUS_OP', 'MINUS_OP']:
            self.advance()
            self.term()

    def term(self):
        self.factor()
        while self.current_token() and self.current_token()[0] in ['MULT_OP', 'DIV_OP']:
            self.advance()
            self.factor()

    def factor(self):
        token = self.current_token()
        if token[0] == 'IDENTIFIER':
            self.advance()
        elif token[0].startswith('HEX_') or token[0] in ['ENTERO', 'FLOTANTE']:
            self.advance()
        elif token[0] == 'LPAREN_SPEC':
            self.advance()
            self.expression()
            self.expect('RPAREN_SPEC')
        else:
            raise SyntaxError(f"Factor inesperado: {token}")

    def block(self):
        self.expect('LBRACE_SPEC')
        while self.current_token() and self.current_token()[0] != 'RBRACE_SPEC':
            self.statement()
            self.expect('SEMICOLON_SPEC')
        self.expect('RBRACE_SPEC')
