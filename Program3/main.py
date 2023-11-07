from MyProgram import Lexer, Parser, ParenthesisMatcher, Error

# Search for a .txt file in the current directory
file_name = "Expression.txt"
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
