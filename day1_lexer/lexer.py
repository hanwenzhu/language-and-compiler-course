import re
import importlib

from .errors import LexerError
from .presets import TokenType, load_source_file


KEYWORD_REGEX = r'(?P<keyword>if|else|while|decl|return|break|continue)'
LITERAL_REGEX = r'(?P<literal>[0-9]+|"[^"]*"|TRUE|FALSE|NONE)'
IDENTIFIER_REGEX = r'(?P<identifier>[a-zA-Z_][a-zA-Z0-9_]*)'
SYMBOL_REGEX = r'(?P<symbol>,|;|\(|\)|{|})'
OPERATOR_REGEX = r'(?P<operator>\|\||&&|==|!=|<=|>=|<|>|\+|-|\*|/|!|=)'
WHITESPACE_REGEX = r'(?P<whitespace>\s+)'

ALL_REGEXES = [KEYWORD_REGEX, LITERAL_REGEX, IDENTIFIER_REGEX,
               SYMBOL_REGEX, OPERATOR_REGEX, WHITESPACE_REGEX]

SYNTAX_REGEX = re.compile(r'|'.join(ALL_REGEXES))


def lex(raw_code: str) -> [(str, TokenType)]:
    """
    Lexes the given string according to the described syntax.
    Note that this function should automatically strip whitespace tokens.

    return: a list of (token_str, TokenType)

    Example:
        input: "main() {decl a;}"
        output: [
            ('main', TokenType.IDENTIFIER),
            ('(', TokenType.SYMBOL),
            (')', TokenType.SYMBOL),
            ('{', TokenType.SYMBOL),
            ('decl', TokenType.KEYWORD),
            ('a', TokenType.IDENTIFIER),
            (';', TokenType.SYMBOL),
            ('}', TokenType.SYMBOL)
        ]
    """

    output = []

    for match in SYNTAX_REGEX.finditer(raw_code):
        if match is None:
            raise LexerError('program doesn even lex idk why just fix ur code')

        matched = match.groupdict().items()
        ((token_type_str, token_str),) = [
            (t, s) for (t, s) in matched if s is not None]
        token_type = TokenType(token_type_str)

        if token_type == TokenType.WHITESPACE:
            continue

        output.append((token_str, token_type))

    return output
