import re
import random
from typing import List

# derived from https://github.com/zekedroid/ABC-Music-Player/blob/master/src/grammar/ABCMusic.g4

SIMPLE_ABC_GRAMMAR = {
    "<start>": ["<INDEX><TITLE><COMPOSER><LENGTH><KEY><VERSES>"],
    "<NEWLINE>": ["\n"],
    "<NUMBER>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<TAKT_LENGTH>": ["6/4", "4/4", "8/4", "8/8", "1/8"],
    "<NUMBER_COMBI>": ["<NUMBER>", "<NUMBER_COMBI><NUMBER>"],
    "<SMALL_Letter>": [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ],
    "<BIG_Letter>": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ],
    "<INDEX>": ["X:<NUMBER_COMBI><NEWLINE>"],
    "<SPECIAL_CHARS>": ["?", "!", '"', "$", "%", "?", "(", ")"],
    "<NAME>": [
        "<BIG_Letter>",
        "<SMALL_Letter>",
        "<NAME><SMALL_Letter>",
        "<NAME><BIG_Letter>",
    ],
    "<TITLE_NAME>": [
        "<BIG_Letter>",
        "<SMALL_Letter>",
        "<SPECIAL_CHARS>",
        "<TITLE_NAME><BIG_Letter>",
        "<TITLE_NAME><SMALL_Letter>",
        "<TITLE_NAME><SPECIAL_CHARS>",
    ],
    "<TITLE>": ["T: <TITLE_NAME><NEWLINE>"],
    "<COMPOSER>": ["C: <NAME><NEWLINE>"],
    "<LENGTH>": ["L: <TAKT_LENGTH><NEWLINE>"],
    "<MUSICNOTATION>": ["#", "b"],
    "<A_G>": ["A", "B", "C", "D", "E", "F", "G"],
    "<a_g>": ["a", "b", "c", "d", "e", "f", "g"],
    "<KEY>": [
        "K: <A_G><MUSICNOTATION><NEWLINE>",
        "K: <A_G><NEWLINE>",
        "K: <a_g><NEWLINE>",
        "K: <a_g><MUSICNOTATION><NEWLINE>",
    ],
    "<TAKT_SINGLE>": [
        "<a_g><a_g>",
        "<a_g>2",
    ],
    "<TAKT>": ["<TAKT_SINGLE><TAKT_SINGLE>"],
    "<TAKT_ENDING>": ["|\\ ", ":| "],
    "<VERSE>": ["<TAKT> | <TAKT> | <TAKT> | <TAKT> <TAKT_ENDING>"],
    "<VERSES>": ["<VERSE>", "<VERSES><VERSE>"],
}

RE_NONTERMINAL = re.compile(r"(<[^<> ]*>)")
START_SYMBOL = "<start>"


def nonterminals(expansion):
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return re.findall(RE_NONTERMINAL, expansion)


def is_nonterminal(s):
    return re.match(RE_NONTERMINAL, s)


class ExpansionError(Exception):
    pass


def simple_grammar_fuzzer(
    grammar,
    start_symbol=START_SYMBOL,
    max_nonterminals=10,
    max_expansion_trials=100,
    log=False,
):
    term = start_symbol
    expansion_trials = 0

    while len(nonterminals(term)) > 0:
        symbol_to_expand = random.choice(nonterminals(term))
        expansions = grammar[symbol_to_expand]
        expansion = random.choice(expansions)
        new_term = term.replace(symbol_to_expand, expansion, 1)

        if len(nonterminals(new_term)) < max_nonterminals:
            term = new_term
            if log:
                print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
            expansion_trials = 0
        else:
            expansion_trials += 1
            if expansion_trials >= max_expansion_trials:
                term = ""

    return term
