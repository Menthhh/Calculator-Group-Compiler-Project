import sys
from ply import lex

tokens = [
    'REAL', 'INT', 'VAR', 'LIST', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'INTDIV',
    'ASSIGNS', 'NOTEQUALS', 'EQUALS_EQ', 'POW', 'GREATER', 'LESS', 'GREATER_EQ',
    'LESS_EQ', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'ERR'
]

# Define the token rules (regex patterns)
def t_REAL(t):
    r'(\d+\.\d*|\.\d+)([eE][+-]?\d+)?'
    return t

def t_INT(t):
    r'\d+'
    return t

def t_POW(t):
    r'\^'
    return t

def t_LIST(t):
    r'list'
    t.type = 'LIST'
    return t

def t_VAR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_NOTEQUALS(t):
    r'!='
    return t

def t_EQUALS_EQ(t):
    r'=='
    return t

def t_ASSIGNS(t):
    r'='
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_INTDIV(t):
    r'//'
    return t

def t_DIVIDE(t):
    r'/'
    return t

def t_GREATER_EQ(t):
    r'>='
    return t
def t_GREATER(t):
    r'>'
    return t

def t_LESS_EQ(t):
    r'<='
    return t

def t_LESS(t):
    r'<'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t

t_ignore = ' \t'

# Error handling for unrecognized characters
def t_error(t):
    t.type = 'ERR'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

# Create the lexer
lexer = lex.lex()

# Format token function to match the output format
def format_token(token):
    """Format token according to the required output format"""
    if token.type == 'PLUS':
        return '+/+'  
    elif token.type == 'MINUS':
        return '-/-'
    elif token.type == 'TIMES':
        return '*/*'
    elif token.type == 'DIVIDE':
        return '/'  
    elif token.type == 'INTDIV':
        return '///INT_DIVISION'  
    elif token.type == 'EQUALS_EQ':
        return '==/EQUAL'  
    elif token.type == 'ASSIGNS':
        return '=/='
    elif token.type == 'NOTEQUALS':
        return '!=/!='  
    elif token.type == 'POW':
        return '^/POW'  
    elif token.type == 'GREATER':
        return '>/GREATER'
    elif token.type == 'GREATER_EQ':
        return '>=/GREATER_EQ'
    elif token.type == 'LESS':
        return '< /LESS'
    elif token.type == 'LESS_EQ':
        return '<=/LESS_EQ'
    elif token.type == 'LPAREN':
        return '(/LPAREN'
    elif token.type == 'RPAREN':
        return ')/RPAREN'
    elif token.type == 'LBRACKET':
        return '[/LBRACKET'
    elif token.type == 'RBRACKET':
        return ']/RBRACKET'
    elif token.type == 'LIST':
        return 'list/list'
    elif token.type == 'VAR':
        return f"{token.value}/VAR"
    elif token.type == 'INT':
        return f"{token.value}/INT"
    elif token.type == 'REAL':
        return f"{token.value}/REAL"
    else:
        return f"{token.value}/{token.type}"

# Function to process the input file and write the output
def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Could not open input file '{input_file}'")
        return

    try:
        with open(output_file, 'w') as f:
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                lexer.input(line)
                tokens = []
                
                while True:
                    tok = lexer.token()
                    if not tok:
                        break
                    tokens.append(format_token(tok))
                
                f.write(' '.join(tokens) + '\n')
    except IOError:
        print(f"Error: Could not write to output file '{output_file}'")

# Main function to run the script
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python lexer.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_file(input_file, output_file)
