from MyProgram import Lexer, Parser

while True:
        text = input("RR_int> ")
        if text == "q":
            break
        lexer = Lexer(text)
        tokens, errors = lexer.make_tokens()
        if tokens:
            print("Inputed Text: ", text)
            print("Generated Tokens: ", tokens)
            parser = Parser(tokens)
            try:
                result = parser.parse()
                print("Expression Tree:", result)
            except Exception as e:
                print("Parsing Error:", str(e))
        else:
            print(errors.display())