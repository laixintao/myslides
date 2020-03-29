from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.lexers import SimpleLexer
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter

from prompt_toolkit.contrib.regular_languages import compile, lexer, completion

redis_grammar = compile(r"\s* (?P<command>(SET|set|GET|get)) \s+ (?P<args>.*) \s*")
mylexer = lexer.GrammarLexer(
    redis_grammar,
    lexers={
        "command": SimpleLexer("class:keyword"),
        "args": SimpleLexer("class:string"),
    },
)
free_style = Style.from_dict({"keyword": "green", "string": "blue"})

command_completer = WordCompleter(
    ["GET", "SET", "SETNX", "SETXX", "SETABC"], ignore_case=True
)

my_completer = completion.GrammarCompleter(
    redis_grammar, {"command": command_completer}
)


def repl():
    while 1:
        try:
            user_input = prompt(
                "redis> ",
                history=FileHistory(".iredis_history"),
                auto_suggest=AutoSuggestFromHistory(),
                lexer=mylexer,
                style=free_style,
                completer=my_completer,
            )
        except EOFError:
            print("Goodbye!")
            return
        print(user_input)


repl()
