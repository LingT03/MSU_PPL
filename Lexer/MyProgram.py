# Initialize the text to tokenize
RR_int = "RR_int"
RR_float = "RR_float"
RR_plus = "RR_plus"
RR_minus = "RR_minus"
RR_mul = "RR_mul"
RR_div = "RR_div"
DIGITS = '0123456789'

class Token:
    # Token class to store the token type and value
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

    def __repr__(self):
        # Return a string representation of the class instance
        return f"Token(value={self.value}, token_type='{self.token_type}')"

# Lexer class
class Lexer:
    # init function to initialize the text, position, and current_character
    def __init__(self, text):
        self.text = text
        self.position = 0  # Starting position
        self.current_character = self.text[self.position]  # current character of text

    def advance(self):
        # function to move to the next character
        self.position += 1  # increment position
        if self.position >= len(self.text):  # if we're at the end of the text
            self.current_character = None  # set current_character to None (no more characters to read)
        else:
            self.current_character = self.text[self.position]  # otherwise, set current_character to the next character in the text

    def make_tokens(self):
        # function to make tokens
        tokens = []  # list to store tokens

        while self.current_character is not None:
            # while we're not at the end of the text
            # print statements to help with debugging

                if self.current_character.isspace():
                    # if space ignore and move to next character
                    self.advance()
                elif self.current_character in DIGITS:
                    # if digit, append the digits to the tokens list
                    tokens.append(self.make_digits())
                elif self.current_character == '+':
                    # if plus sign, append RR_plus to the tokens list
                    tokens.append(RR_plus)
                    self.advance()
                elif self.current_character == '-':
                    # if minus sign, append RR_minus to the tokens list
                    tokens.append(RR_minus)
                    self.advance()
                elif self.current_character == '*':
                    # if multiplication sign, append RR_mul to the tokens list
                    tokens.append(RR_mul)
                    self.advance()
                elif self.current_character == '/':
                    # if division sign, append RR_div to the tokens list
                    tokens.append(RR_div)
                    self.advance()
                else:
                    char = self.current_character
                    pos_start = self.position
                    self.advance()
                    pos_end = self.position
                    self.advance()
                    return [], IllegalCharError( pos_start, pos_end, "'" + char + "'")

        return tokens, None

    def make_digits(self):
        # function to check if the Digit is an int or float
        dig_str = ""  # string to store the digits
        dot_cnt = 0  # Dot counter

        while self.current_character is not None and (self.current_character in DIGITS or self.current_character == '.'):
            # while we're not at the end of the text and the current character is a digit or a dot
            if self.current_character == '.':
                # if dot increment dot counter
                dot_cnt += 1
            dig_str += self.current_character
            self.advance()

            if dot_cnt > 1:
                # if there is more than one dot, raise an error
                return self.make_error("Invalid float: multiple dots")

        if dot_cnt == 0:  # no dot = int
            return (RR_int, int(dig_str))

        elif dot_cnt == 1:  # one dot = float
            return (RR_float, float(dig_str))

    def make_error(self, message):
        pos_start = self.position
        pos_end = self.position + 1
        return IllegalCharError(pos_start, pos_end, message)

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        # Return a string representation of the class instance
        result = f'{self.error_name}: {self.details}\n'
        result += f'From Column: {self.pos_start},  To Column: {self.pos_end + 1}'

        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class NumberNode:
    def __init__(self,token):
        self.token = token

    def __repr__(self):
        return f'NumberNode({self.token.value})'


class OperationNode:
    def __init__(self, left_node, operator_token, right_node):
        self.left_node = left_node
        self.operator_token = operator_token
        self.right_node = right_node

    def __repr__(self):
        return f'OperationNode({self.left_node}, {self.operator_token.value}, {self.right_node})'


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = -1
        self.advance()

    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]
        return self.current_token
    
    def parse (self):
        expression = []

        while self.current_token is not None:
            print ("Parsing...", self.current_token)
            self.advance()
            if self.current_token == RR_int or self.current_token == RR_float:
                self.factor()
                print("factored")
            elif self.current_token == RR_plus or self.current_token == RR_minus:
                self.term()
                print("termed")
            elif self.current_token == RR_mul or self.current_token == RR_div:
                self.expression()
                print("expressed")
            elif self.current_token == None:
                print("Parsing Complete")
                break
            else:
                print("error token:", self.current_token)
                raise Exception("Parsing Error: Invalid Token")
            self.advance()

        
                        

    def factor(self):
        current_token = self.current_token

        if current_token == RR_int or current_token == RR_float:
            self.advance()
            return NumberNode(current_token)

    def term(self):
        left = self.factor()
        opTree = self.factor()

        while self.current_token == RR_mul or self.current_token == RR_div:
            operator_token = self.current_token
            self.advance()
            right = self.factor()
            opTree = OperationNode(left, operator_token, right)

        return opTree

    def expression(self):
        left = self.term()
        opTree = self.term()

        while self.current_token == RR_plus or self.current_token == RR_minus:
            operator_token = self.current_token
            self.advance()
            right = self.term()
            opTree = OperationNode(left, operator_token, right)

        return opTree

if __name__ == "__main__":
    while True:
        # while True, ask for input and tokenize it
        text = input("RR_int> ")
        if text == "q":
            # if exit, break out of the loop
            break
        lexer = Lexer(text)
        tokens, errors = lexer.make_tokens()
        if tokens: # For Tokenizing
            print("Inputed Text: ", text)
            print("Generated Tokens: ", tokens)  # Print each error separately
            parser = Parser(tokens)
            try:
                result = parser.parse()
                print("Expression Tree:", result)
            except Exception as e:
                print("Parsing Error:", str(e))
        else:
            print(errors.as_string())