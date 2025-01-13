class SymbolTable:
    def __init__(self):
        self.table = {}
        
    def add_entry(self, lexeme, line_num, start_pos, length, type_, value=None):
        self.table[lexeme] = {
            'line_number': line_num,
            'start_pos': start_pos,
            'length': length,
            'type': type_,
            'value': value
        }
    
    def get_entry(self, lexeme):
        return self.table.get(lexeme)
    
    def to_csv(self, filename):
        with open(filename, 'w') as f:
            f.write("lexeme,line_number,start_pos,length,type,value\n")
            for lexeme, entry in self.table.items():
                f.write(f"{lexeme},{entry['line_number']},{entry['start_pos']},"
                       f"{entry['length']},{entry['type']},{entry['value']}\n")