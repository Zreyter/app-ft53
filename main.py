from parser import Parser


def load_tokens():
    tokens = []
    with open("tokens_output.py", 'r') as f:
        for line in f:
            if line.strip().startswith("LexToken"):
                parts = line.strip().split(',')
                token_type = parts[0].split('(')[1]
                token_value = parts[1].strip().strip("'")
                tokens.append((token_type, token_value))
    return tokens


if __name__ == "__main__":
    # Manteniendo el flujo original del lexer
    from lexer import analyze_file

    file_path = "C:/Users/josee/OneDrive/Documentos/Trabajos ITP/Lenguajes y automatas I/code.txt"
    print(f"Analizando el archivo: {file_path}")
    analyze_file(file_path)

    # Carga del archivo de tokens para el parser
    print("Cargando tokens desde el archivo generado...")
    tokens = load_tokens()

    print("Ejecutando el analizador sintáctico...")
    parser = Parser(tokens)
    parser.parse()
