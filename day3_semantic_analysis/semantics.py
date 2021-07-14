from day1_lexer import (
    UndeclaredIdentifierError,
    DuplicateDeclarationError,
    MisplacedControlFlowError
)
from day2_parser import *

from .semantic_context import SemanticContext


def analysis(node: Program):
    """
    Returns nothing if the code is valid; otherwise throws an according error.

    Also prepares the nodes (e.g. populate fields, resolve dependencies) for
    code generation.
    """

    context = SemanticContext()
    node.analysis_pass(context)