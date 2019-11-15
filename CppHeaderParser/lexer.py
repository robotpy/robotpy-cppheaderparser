import ply.lex as lex
import re

_line_re = re.compile(r'^#line (\d+) "(.*)"')


class Lexer(object):

    tokens = [
        "NUMBER",
        "FLOAT_NUMBER",
        "TEMPLATE_NAME",
        "NAME",
        "OPEN_PAREN",
        "CLOSE_PAREN",
        "OPEN_BRACE",
        "CLOSE_BRACE",
        "OPEN_SQUARE_BRACKET",
        "CLOSE_SQUARE_BRACKET",
        "COLON",
        "SEMI_COLON",
        "COMMA",
        "TAB",
        "BACKSLASH",
        "PIPE",
        "PERCENT",
        "EXCLAMATION",
        "CARET",
        "COMMENT_SINGLELINE",
        "COMMENT_MULTILINE",
        "PRECOMP_MACRO",
        "PRECOMP_MACRO_CONT",
        "ASTERISK",
        "AMPERSAND",
        "EQUALS",
        "MINUS",
        "PLUS",
        "DIVIDE",
        "CHAR_LITERAL",
        "STRING_LITERAL",
        "NEW_LINE",
        "SQUOTE",
        "ELLIPSIS",
        "DOT",
    ]

    t_ignore = " \r?@\f"
    t_NUMBER = r"[0-9][0-9XxA-Fa-f]*"
    t_FLOAT_NUMBER = r"[-+]?[0-9]*\.[0-9]+([eE][-+]?[0-9]+)?"
    t_TEMPLATE_NAME = r"CppHeaderParser_template_[0-9]+"
    t_NAME = r"[<>A-Za-z_~][A-Za-z0-9_]*"
    t_OPEN_PAREN = r"\("
    t_CLOSE_PAREN = r"\)"
    t_OPEN_BRACE = r"{"
    t_CLOSE_BRACE = r"}"
    t_OPEN_SQUARE_BRACKET = r"\["
    t_CLOSE_SQUARE_BRACKET = r"\]"
    t_SEMI_COLON = r";"
    t_COLON = r":"
    t_COMMA = r","
    t_TAB = r"\t"
    t_BACKSLASH = r"\\"
    t_PIPE = r"\|"
    t_PERCENT = r"%"
    t_CARET = r"\^"
    t_EXCLAMATION = r"!"

    def t_PRECOMP_MACRO(self, t):
        r"\#.*"
        m = _line_re.match(t.value)
        if m:
            self.filename = m.group(2)
            self.line_offset = 1 + self.lex.lineno - int(m.group(1))
        else:
            return t

    t_PRECOMP_MACRO_CONT = r".*\\\n"

    def t_COMMENT_SINGLELINE(self, t):
        r"\/\/.*\n?"
        if t.value.startswith("///") or t.value.startswith("//!"):
            if self.doxygenCommentCache:
                self.doxygenCommentCache += "\n"
            if t.value.endswith("\n"):
                self.doxygenCommentCache += t.value[:-1]
            else:
                self.doxygenCommentCache += t.value
        t.lexer.lineno += t.value.count("\n")

    t_ASTERISK = r"\*"
    t_MINUS = r"\-"
    t_PLUS = r"\+"
    t_DIVIDE = r"/(?!/)"
    t_AMPERSAND = r"&"
    t_EQUALS = r"="
    t_CHAR_LITERAL = "'.'"
    t_SQUOTE = "'"
    t_ELLIPSIS = r"\.\.\."
    t_DOT = r"\."

    # found at http://wordaligned.org/articles/string-literals-and-regular-expressions
    # TODO: This does not work with the string "bla \" bla"
    t_STRING_LITERAL = r'"([^"\\]|\\.)*"'

    # Found at http://ostermiller.org/findcomment.html
    def t_COMMENT_MULTILINE(self, t):
        r"/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/"
        if t.value.startswith("/**") or t.value.startswith("/*!"):
            # not sure why, but get double new lines
            v = t.value.replace("\n\n", "\n")
            # strip prefixing whitespace
            v = re.sub("\n[\\s]+\\*", "\n*", v)
            self.doxygenCommentCache += v
        t.lexer.lineno += len([a for a in t.value if a == "\n"])

    def t_NEWLINE(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_error(self, v):
        print("Lex error: ", v)

    def __init__(self, filename):
        self.lex = lex.lex(module=self)
        self.input = self.lex.input
        self.token = self.lex.token

        # For tracking current file/line position
        self.filename = filename
        self.line_offset = 0

        # Doxygen comments
        self.doxygenCommentCache = ""

    def current_location(self):
        return self.filename, self.lex.lineno - self.line_offset

    def get_doxygen(self):
        doxygen = self.doxygenCommentCache
        self.doxygenCommentCache = ""
        return doxygen


if __name__ == "__main__":
    lex.runmain(lexer=Lexer())
