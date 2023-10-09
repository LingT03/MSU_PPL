from MyProgram import Lexer, Parser, ParenthesisMatcher, Error

# Search for a .txt file in the current directory
file_name = "Grammar.txt"
if file_name:
    with open(file_name, 'r') as file:
        for line in file:
            text = line.strip()
            # check line for parenthesis matching
            matcher = ParenthesisMatcher()
            if not matcher.is_balanced(text):
                print("Parenthesis Error: Unbalanced Parenthesis")
                break
            lexer = Lexer(text, file_name)
            tokens, errors = lexer.make_tokens()
            if tokens:
                print("Input Text: ", text)
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
