%{
#include <stdio.h>
%}

/* Tokens */
%token INT REAL VAR LIST
%token PLUS MINUS TIMES DIVIDE
%token EQUALS NOTEQUALS
%token POW
%token GREATER LESS GREATER_EQ LESS_EQ
%token LPAREN RPAREN
%token LBRACKET RBRACKET
%token ERR

/* Regular Expressions for Tokens */
REAL            [0-9]+\.[0-9]*([eE][+-]?[0-9]+)?|\.[0-9]+([eE][+-]?[0-9]+)?
INT             [0-9]+
VAR             [a-zA-Z][a-zA-Z0-9]*
LIST            list
POW             \^
NOTEQUALS       !=
EQUALS          =
PLUS            \+
MINUS           -
TIMES           \*
DIVIDE          /
GREATER         >
LESS            <
GREATER_EQ      >=
LESS_EQ         <=
LPAREN          \(
RPAREN          \)
LBRACKET        \[
RBRACKET        \]
WHITESPACE      [ \t\n]+  /* Matches one or more spaces, tabs, or newline characters */

/* Actions */
%%

{REAL}          { return REAL; }
{INT}           { return INT; }
{VAR}           { return VAR; }
{LIST}          { return LIST; }
{POW}           { return POW; }
{NOTEQUALS}     { return NOTEQUALS; }
{EQUALS}        { return EQUALS; }
{PLUS}          { return PLUS; }
{MINUS}         { return MINUS; }
{TIMES}         { return TIMES; }
{DIVIDE}        { return DIVIDE; }
{GREATER}       { return GREATER; }
{LESS}          { return LESS; }
{GREATER_EQ}    { return GREATER_EQ; }
{LESS_EQ}       { return LESS_EQ; }
{LPAREN}        { return LPAREN; }
{RPAREN}        { return RPAREN; }
{LBRACKET}      { return LBRACKET; }
{RBRACKET}      { return RBRACKET; }
{WHITESPACE}    { /* Ignore whitespace (spaces, tabs, newlines) */ }

.               { return ERR; }

%%

int yywrap() {
    return 1;
}
