%{
#include <stdio.h>
%}

/* Tokens */
%token INT REAL VAR LIST
%token PLUS MINUS TIMES DIVIDE
%token EQUALS NOTEQUALS
%token POW
%token LPAREN RPAREN
%token LBRACKET RBRACKET
%token ERR

/* Regular Expressions for Tokens */
REAL            [0-9]+\.[0-9]*|\.[0-9]+
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
LPAREN          \(
RPAREN          \)
LBRACKET        \[
RBRACKET        \]
WHITESPACE      [ \t]+

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
{LPAREN}        { return LPAREN; }
{RPAREN}        { return RPAREN; }
{LBRACKET}      { return LBRACKET; }
{RBRACKET}      { return RBRACKET; }
{WHITESPACE}    { /* Ignore whitespace */ }

.               { return ERR; }

%%

int yywrap() {
    return 1;
}