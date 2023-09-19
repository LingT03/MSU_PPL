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

if __name__ == "__main__":
    while True:
        # while True, ask for input and tokenize it
        text = input("RR_int> ")
        lexer = Lexer(text)
        tokens, errors = lexer.make_tokens()
        if errors:
            print(errors.as_string())  # Print each error separately
        else:
            print("Inputed Text: ", text)
            print("Generated Tokens: ", tokens)
