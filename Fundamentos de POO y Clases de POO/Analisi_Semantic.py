import re

class CodeTokenizer:
    def __init__(self):
        self.patterns = [
            (r"[\+\-]?[0-9]+\.[0-9]+", "NUMDB"),
            (r"[\+\-]?[0-9]+", "NUMINT"),
            (r"\bcase\b", "CASE"),
            (r"\bswitch\b", "SWTCH"),
            (r"\bbreak\b", "BRK"),
            (r"\btry\b", "TRY"),
            (r"\binput\b", "INP"),
            (r"\boutput\b", "OUT"),
            (r"\bclear\b", "CLEAR"),
            (r"\bint\b", "TPINT"),
            (r"\bstring\b", "TPSTR"),
            (r"\bdouble\b", "TPDBL"),
            (r"\bcatch\b", "CTCH"),
            (r"\bif\b", "IF"),
            (r"\belse\b", "ELSE"),
            (r"\belseif\b", "ELIF"),
            (r"\bfor\b", "FOR"),
            (r"\bwhile\b", "WHI"),
            (r"\bdo\b", "DO"),
            (r"\bcontinue\b", "CNTN"),
            (r"\breturn\b", "RTRN"),
            (r"\bfunction\b", "FCTN"),
            (r"\b[_][a-zA-Z_][a-zA-Z0-9_]*\b", "IDEN"),
            (r"[;]", "CH;"),
            (r"[,]", "CH,"),
            (r"[.]", "CH."),
            (r"[(]", "CH("),
            (r"[)]", "CH)"),
            (r"[{]", "CH{"),
            (r"[}]", "CH}"),
            (r"[=]", "ASSGN"),
            (r"[+]", "AOP+"),
            (r"[-]", "AOP-"),
            (r"[*]", "AOP*"),
            (r"[<]", "ROP<"),
            (r"[>]", "ROP>"),
            (r"[!]", "LOP!"),
            (r"[&]", "LOP&"),
            (r"[|]", "LOP|"),
            (r"[:]", "CH:"),
            (r"==", "ROP=="),
            (r"!=", "ROP!="),
            (r"<=", "ROP<="),
            (r">=", "ROP>="),
            (r"\n", "BRKLN"),
            (r"//.*", "COMM"),
            (r'".*"', "STR"),
            (r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", "IDEN"),  # Identificadores normales
            (r"\s+", None),  # Espacios en blanco (ignorar)
        ]
        
        # Compilar todas las expresiones regulares
        self.regex_patterns = [(re.compile(pattern), token_type) 
                             for pattern, token_type in self.patterns]

    def tokenize_code(self, code: str) -> list:
        """Convierte el código en una lista de tokens"""
        tokens = []
        pos = 0
        code_length = len(code)
        
        while pos < code_length:
            match = None
            for pattern, token_type in self.regex_patterns:
                regex_match = pattern.match(code, pos)
                if regex_match:
                    # Si encontramos un match
                    value = regex_match.group(0)
                    if token_type is not None:  # Ignorar espacios en blanco
                        tokens.append((value, token_type))
                    pos = regex_match.end()
                    match = value
                    break
            
            if not match:
                # Si no encontramos ningún patrón que coincida
                raise SyntaxError(f"Carácter no reconocido: '{code[pos]}' en posición {pos}")
        
        return tokens

    def tokenize_variable_content(self, variable_content: str) -> list:
        """Método específico para tokenizar el contenido de una variable"""
        return self.tokenize_code(variable_content)


# Ejemplo de uso
if __name__ == "__main__":
    tokenizer = CodeTokenizer()
    
    # El texto que proporcionaste dentro de la variable
    code_text = 'int x = 10; if ( x > 5 { int x = 5; }'
    
    try:
        tokens = tokenizer.tokenize_variable_content(code_text)
        
        print("Tokens generados:")
        for token in tokens:
            print(f"{token[0]:<10} -> {token[1]}")
        
        print("\nLista completa de tokens:")
        print(tokens)
        
    except SyntaxError as e:
        print(f"Error de tokenización: {e}")

class SemanticValidator:
    def __init__(self):
        # Definición de todos los caminos semánticos válidos
        self.valid_paths = {
            # IN01 - Declaraciones de variables
            "TPINT": [("IDEN", "ASSGN", ("NUMINT", "NUMDB", "IDEN"), "CH;")],
            "TPSTR": [("IDEN", "ASSGN", ("STR", "IDEN"), "CH;")],
            "TPDBL": [("IDEN", "ASSGN", ("NUMDB", "IDEN"), "CH;")],
            
            # IN05 - Asignaciones
            "ASSGN": [
                ("IDEN", "ASSGN", ("NUMINT", "NUMDB", "STR", "IDEN"), "CH;"),
                ("IDEN", "ASSGN", "IDEN", ("AOP+", "AOP-", "AOP*", "AOP/"), 
                 ("NUMINT", "NUMDB", "IDEN"), "CH;")
            ],
            
            # IN08 - Estructuras IF
            "IF": [
                ("IF", "CH(", "IDEN", ("ROP<", "ROP>", "ROP<=", "ROP>=", "ROP==", "ROP!="), 
                 ("NUMINT", "NUMDB", "IDEN"), "CH)", "CH{", 
                 ("TPINT", "TPSTR", "TPDBL", "IDEN", "IF", "FOR", "WHI", "DO"), "CH}")
            ],
            
            # IN13 - Estructuras FOR
            "FOR": [
                ("FOR", "CH(", "TPINT", "IDEN", "ASSGN", "NUMINT", "CH;",
                 "IDEN", ("ROP<", "ROP>", "ROP<=", "ROP>=", "ROP==", "ROP!="), 
                 "NUMINT", "CH;", "IDEN", "ASSGN", "IDEN", 
                 ("AOP+", "AOP-", "AOP*", "AOP/"), "NUMINT", "CH)", "CH{",
                 ("TPINT", "TPSTR", "TPDBL", "IDEN", "IF", "FOR", "WHI", "DO"), "CH}")
            ],
            
            # IN02 - Operaciones aritméticas
            "AOP+": [("IDEN", "AOP+", ("NUMINT", "NUMDB", "IDEN"))],
            "AOP-": [("IDEN", "AOP-", ("NUMINT", "NUMDB", "IDEN"))],
            "AOP*": [("IDEN", "AOP*", ("NUMINT", "NUMDB", "IDEN"))],
            "AOP/": [("IDEN", "AOP/", ("NUMINT", "NUMDB", "IDEN"))],
            
            # IN04 - Operadores relacionales
            "ROP<": [("IDEN", "ROP<", ("NUMINT", "NUMDB", "IDEN"))],
            "ROP>": [("IDEN", "ROP>", ("NUMINT", "NUMDB", "IDEN"))],
            "ROP<=": [("IDEN", "ROP<=", ("NUMINT", "NUMDB", "IDEN"))],
            "ROP>=": [("IDEN", "ROP>=", ("NUMINT", "NUMDB", "IDEN"))],
            "ROP==": [("IDEN", "ROP==", ("NUMINT", "NUMDB", "IDEN", "STR"))],
            "ROP!=": [("IDEN", "ROP!=", ("NUMINT", "NUMDB", "IDEN", "STR"))],
            
            # IN03 - Operadores lógicos
            "LOP!": [("LOP!", ("IDEN", "NUMINT", "NUMDB", "STR"))],
            "LOP&": [("IDEN", "LOP&", "IDEN")],
            "LOP|": [("IDEN", "LOP|", "IDEN")]
        }

    def validate_tokens(self, tokens: list) -> bool:
        """Valida si la secuencia de tokens sigue un camino semántico válido"""
        i = 0
        n = len(tokens)
        
        while i < n:
            current_token, current_type = tokens[i]
            
            if current_type in self.valid_paths:
                valid_sequences = self.valid_paths[current_type]
                matched = False
                
                for sequence in valid_sequences:
                    seq_len = len(sequence)
                    if i + seq_len > n:
                        continue
                    
                    match = True
                    for j in range(seq_len):
                        expected = sequence[j]
                        actual_type = tokens[i + j][1]
                        
                        # Si el expected es una tupla, comprobar si el tipo actual está en ella
                        if isinstance(expected, tuple):
                            if actual_type not in expected:
                                match = False
                                break
                        elif actual_type != expected:
                            match = False
                            break
                    
                    if match:
                        i += seq_len
                        matched = True
                        break
                
                if not matched:
                    # Mostrar información detallada del error
                    expected_str = " o ".join([str(seq) for seq in valid_sequences])
                    context_start = max(0, i-2)
                    context_end = min(n, i+3)
                    context = " ".join([f"{tok}({typ})" for tok, typ in tokens[context_start:context_end]])
                    
                    raise SyntaxError(
                        f"Error semántico en '{current_token}'\n"
                        f"Se esperaba una de estas secuencias después de {current_type}:\n"
                        f"{expected_str}\n"
                        f"Contexto: {context}"
                    )
            else:
                i += 1
        
        return True

# Ejemplo de uso combinado con el tokenizador anterior
if __name__ == "__main__":
    # Tu ejemplo de código
    code_text = 'int x = 10; if ( x > 5 ) { int y = 5; }'
    
    # Tokenizar
    tokenizer = CodeTokenizer()
    try:
        tokens = tokenizer.tokenize_variable_content(code_text)
        print("Tokens generados:")
        for token in tokens:
            print(f"{token[0]:<10} -> {token[1]}")
        
        # Validar semántica
        validator = SemanticValidator()
        is_valid = validator.validate_tokens(tokens)
        
        if is_valid:
            print("\n✅ El código es semánticamente válido!")
        else:
            print("\n❌ El código tiene errores semánticos")
            
    except SyntaxError as e:
        print(f"\n❌ Error: {e}")