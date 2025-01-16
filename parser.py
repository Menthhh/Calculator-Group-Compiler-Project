import sys
from ply import lex, yacc
from symbolTable import SymbolTable

symbol_table = SymbolTable()
current_line = 1
current_pos = 0

def set_pos():
    global current_pos
    current_pos += 1

def parse_lex_file(lex_file_path):
    tokens = []
    with open(lex_file_path, 'r') as f:
        for line in f:
            if line.startswith('%token'):
                tokens.extend(line.split()[1:])
    return tokens

tokens = parse_lex_file('shadowSparks.lex')

# Define the token rules (regex patterns)
def t_REAL(t):
    r'(\d+\.\d*|\.\d+)([eE][+-]?\d+)?'
    set_pos()
    return t

def t_INT(t):
    r'[1-9]\d*|0'
    set_pos()
    return t

def t_POW(t):
    r'\^'
    set_pos()
    return t

def t_LIST(t):
    r'list\b'
    t.type = 'LIST'
    set_pos()
    return t

def t_VAR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    set_pos()
    return t

def t_NOTEQUALS(t):
    r'!='
    set_pos()
    return t

def t_EQUALS_EQ(t):
    r'=='
    set_pos()
    return t

def t_ASSIGNS(t):
    r'='
    set_pos()
    return t

def t_PLUS(t):
    r'\+'
    set_pos()
    return t

def t_MINUS(t):
    r'-'
    set_pos()
    return t

def t_TIMES(t):
    r'\*'
    set_pos()
    return t

def t_INTDIV(t):
    r'//'
    set_pos()
    return t

def t_DIVIDE(t):
    r'/'
    set_pos()
    return t

def t_GREATER_EQ(t):
    r'>='
    set_pos()
    return t
def t_GREATER(t):
    r'>'
    set_pos()
    return t

def t_LESS_EQ(t):
    r'<='
    set_pos()
    return t

def t_LESS(t):
    r'<'
    set_pos()
    return t

def t_LPAREN(t):
    r'\('
    set_pos()
    return t

def t_RPAREN(t):
    r'\)'
    set_pos()
    return t

def t_LBRACKET(t):
    r'\['
    set_pos()
    return t

def t_RBRACKET(t):
    r'\]'
    set_pos()
    return t

t_ignore = ' \t'

# Error handling for unrecognized characters
def t_error(t):
    t.type = 'ERR'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

# Grammar rules
def p_expression(p):
    '''expression : arithmetic_expr
                 | assignment_expr
                 | comparison_expr
                 | list_access'''
    p[0] = p[1]

def p_arithmetic_expr(p):
    '''arithmetic_expr : term
                      | arithmetic_expr PLUS term
                      | arithmetic_expr MINUS term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"({p[1]}{p[2]}{p[3]})"

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor
            | term INTDIV factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"({p[1]}{p[2]}{p[3]})"

def p_factor(p):
    '''factor : atom
              | factor POW atom'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"({p[1]}{p[2]}{p[3]})"

def p_atom(p):
    '''atom : INT
            | REAL
            | VAR
            | list_access
            | LPAREN expression RPAREN'''
    if len(p) == 2:
        if isinstance(p[1], str):
            p[0] = p[1]
            if p.slice[1].type == 'VAR':
                if not symbol_table.get_entry(p[1]):
                    raise NameError(f"Undefined variable {p[1]} at line {current_line}, pos {current_pos}")
        else:
            p[0] = str(p[1])
    else:
        if p[2][0] == '(':
            p[0] = f"{p[2]}"
        else:
            p[0] = f"({p[2]})"

def p_assignment_expr(p):
    '''assignment_expr : VAR ASSIGNS expression
                      | VAR ASSIGNS list_expr
                      | list_access ASSIGNS expression'''
    p[0] = f"({p[1]}{p[2]}{p[3]})"
    if isinstance(p[1], str): 
        symbol_table.add_entry(p[1], current_line, current_pos, len(p[1]), 
                              'VAR' if not isinstance(p[3], list) else 'list', p[3])
    else: 
        var_name = p[1].split('[')[0]
        symbol_table.add_entry(var_name, current_line, current_pos, len(var_name), 'list', p[3])

def p_comparison_expr(p):
    '''comparison_expr : expression EQUALS_EQ expression
                      | expression NOTEQUALS expression
                      | expression GREATER expression
                      | expression GREATER_EQ expression
                      | expression LESS expression
                      | expression LESS_EQ expression'''
    
    p[0] = f"({p[1]}{p[2]}{p[3]})"

def p_list_expr(p):
    '''list_expr : LIST LBRACKET expression RBRACKET'''
    
    p[0] = f"(list[{p[3]}])"

def p_list_access(p):
    '''list_access : VAR LBRACKET expression RBRACKET'''
    
    p[0] = f"({p[1]}[{p[3]}])"

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at line {current_line}, pos {current_pos}: Unexpected token {p.value}")
    else:
        raise SyntaxError(f"Syntax error at line {current_line}, pos {current_pos}: Unexpected end of input")

# Create the lexer
lexer = lex.lex()

# Create the parser
parser = yacc.yacc()

def process_file(input_file, output_file, symbol_table_file):
    global current_line, current_pos
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Could not open input file '{input_file}'")
        return

    try:
        with open(output_file, 'w') as f_out:
            for line_num, line in enumerate(lines, 1):
                current_line = line_num
                current_pos = 0
                line = line.strip()
                if not line:
                    continue
                
                try:
                    result = parser.parse(line, lexer=lexer)
                    f_out.write(f"{result}\n")
                except (SyntaxError, NameError, TypeError) as e:
                    f_out.write(f"{str(e)}\n")
            
        # Write symbol table to CSV
        symbol_table.to_csv(symbol_table_file)
                
    except IOError as e:
        print(f"Error writing to output file: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python combined.py input_file output_file symbol_table_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    symbol_table_file = sys.argv[3]
    process_file(input_file, output_file, symbol_table_file)
