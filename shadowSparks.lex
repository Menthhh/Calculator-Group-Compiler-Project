%{
#include <stdio.h>
%}

/* Tokens */
%token INT REAL VAR LIST
%token PLUS MINUS TIMES DIVIDE INTDIV
%token ASSIGNS NOTEQUALS EQUALS_EQ
%token POW GREATER LESS GREATER_EQ LESS_EQ
%token LPAREN RPAREN LBRACKET RBRACKET
%token ERR

/* Regular Expressions for Tokens */
REAL            [0-9]+\.[0-9]*([eE][+-]?[0-9]+)?|\.[0-9]+([eE][+-]?[0-9]+)?
INT             [1-9][0-9]*|0
VAR             [a-zA-Z][a-zA-Z0-9]*
LIST            list
POW             \^
NOTEQUALS       !=
EQUALS_EQ       ==
EQUALS          =
PLUS            \+
MINUS           -
TIMES           \*
DIVIDE          /
INTDIV          //
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
{EQUALS_EQ}     { return EQUALS_EQ; }
{EQUALS}        { return EQUALS; }
{PLUS}          { return PLUS; }
{MINUS}         { return MINUS; }
{TIMES}         { return TIMES; }
{INTDIV}        { return INTDIV; }
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
