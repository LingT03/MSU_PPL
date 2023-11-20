# Initialize the text to tokenize
RR_int = "RR_int"
RR_float = "RR_float"
RR_plus = "RR_plus"
RR_minus = "RR_minus"
RR_mul = "RR_mul"
RR_div = "RR_div"
RR_OpenPar = "RR_OpenPar"
RR_ClosePar = "RR_ClosePar"
DIGITS = '0123456789'
class Token:
    # Token class to store the token type and value
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

    def __repr__(self):
        # Return a string representation of the class instance
        return f"{self.value}:{self.token_type}"

class Lexer:
    # init function to initialize the text, position, and current_character
    def __init__(self, text, file_name):
        self.text = text
        self.position = 0  # Starting position
        self.current_character = self.text[self.position]  # current character of text
        self.line_num = 1  # line number of the text
        self.file_name = file_name

    def advance(self):
        # function to move to the next character
        self.position += 1  # increment position
        if self.position >= len(self.text):  # if we're at the end of the text
            self.current_character = None  # set current_character to None (no more characters to read)
        else:
            self.current_character = self.text[self.position]
            if self.current_character == "\n":
                self.line_num += 1

    def make_tokens(self):
        # function to make tokens
        tokens = []  # list to store tokens
        errors = [] # list to store errors

        while self.current_character is not None:
            

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
                elif self.current_character == '(':
                    # if open parenthesis, append RR_OpenPar to the tokens list
                    tokens.append(RR_OpenPar)
                    self.advance()
                elif self.current_character == ')':
                    # if close parenthesis, append RR_ClosePar to the tokens list
                    tokens.append(RR_ClosePar)
                    self.advance()
                
            
                else:
                    char = self.current_character
                    errorchar = char
                    err_start = self.position
                    line_num = self.line_num
                    file_name = self.file_name

                    # go through the text until we reach a space a number integer or operator
                    while char is not None and char.isspace() is False and char not in DIGITS and char not in '+-*/':
                        char = self.current_character
                        self.advance()
                        # if we reach the end length of the text, break
                        if self.position >= len(self.text):
                            break

                        err_end = self.position - 1

                    errors.append(SyntaxError(file_name, line_num, err_start, err_end, "'" + errorchar + "'"))

        return tokens, errors

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
                return self.float_error("Invalid float!! multiple dots!")

        if dot_cnt == 0:  # no dot = int
            return Token(RR_int, int(dig_str))

        elif dot_cnt == 1:  # one dot = float
            return Token(RR_float, float(dig_str))

    def float_error(self, error_name):
        # function to catch multiple dots in a float
        result = f'{error_name} Second Dot on COL:{self.current_character}'
        self.advance()
        return result

class ParenthesisMatcher:
    def __init__(self):
        self.stack = []
        self.errors = []

    def is_opening(self, char):
        return char in '([{'

    def is_closing(self, char):
        return char in ')]}'

    def matches(self, open_char, close_char):
        return (open_char == '(' and close_char == ')') or \
               (open_char == '[' and close_char == ']') or \
               (open_char == '{' and close_char == '}')

    def is_balanced(self, input_string):
        for column, char in enumerate(input_string, start=1):
            if self.is_opening(char):
                self.stack.append((char, column))
            elif self.is_closing(char):
                if not self.stack or not self.matches(self.stack[-1][0], char):
                    self.errors.append(ParenthesisError(file_name="Grammar.txt", line_num=1, col_start=column, col_end=column, details="Missing opening parenthesis"))
                else:
                    self.stack.pop()
        while self.stack:
            open_char, column = self.stack.pop()
            self.errors.append(ParenthesisError(file_name="Grammar.txt", line_num=1, col_start=column, col_end=column, details="Missing closing parenthesis"))
        
        return self.errors

class Error:
    def __init__(self, file_name ,line_num, col_start, col_end, error_name, details):
        self.file_name = file_name
        self.line_num = line_num
        self.col_start = col_start
        self.col_end = col_end
        self.error_name = error_name
        self.details = details

    def display(self):

        result = f'File: {self.file_name}, Line: {self.line_num}\n'
        result += f'error name: {self.error_name}, Details: {self.details}\n'
        result += f'Error From COL: {self.col_start},  TO COL: {self.col_end}'

        return result

class SyntaxError(Error):
    def __init__(self, file_name, line_num, col_start, col_end, details):
        super().__init__(file_name, line_num, col_start, col_end, 'Illegal Character', details)

class ParenthesisError(Error):
    def __init__(self, file_name, line_num, col_start, col_end, details):
        super().__init__(file_name, line_num, col_start, col_end, 'Unmatched Parenthesis', details)

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

    def parse (self):
        return self.expression()
        
    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]
            return self.current_token
    
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
# Search for a .txt file in the current directory
file_name = "Expression.txt"

if __name__ == "__main__":
    if file_name:
        with open(file_name, 'r') as file:
            for line in file:
                text = line.strip()
                # Check line for parenthesis matching
                matcher = ParenthesisMatcher()
                errors = matcher.is_balanced(text)

                print("Input Text: ", text)
                
                # Print any parenthesis matching errors
                for error in errors:
                    print(error.display())
                
                if errors:
                    # If there are parenthesis matching errors, break the loop
                    break
                
                lexer = Lexer(text, file_name)
                tokens, errors = lexer.make_tokens()
                if tokens:
                    print("Generated Tokens: ", tokens)
                    parser = Parser(tokens)
                    try:
                        result = parser.parse()
                        print("Expression Tree:", result)
                    except Exception as e:
                        print("Parsing Error:", str(e))
                else:
                    for error in errors:
                        print(error.display())  # Display the error message for each error object
    else:
        print("No .txt file found in the current directory.")
