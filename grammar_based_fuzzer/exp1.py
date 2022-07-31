from fuzzing.fuzzer import Grammar_Fuzzer
from fuzzing.fuzzing_runner import ProgramRunner
from fuzzing.compiler import fuzz_compile, delete_coverage_files
from fuzzing.grammar import SIMPLE_ABC_GRAMMAR, START_SYMBOL
from fuzzing.fuzzing_logger import Logger
import os
import time


def run_grammar_fuzzer(run_time_in_min, dir_path_git, seed_path):
    timeout = 60 * run_time_in_min
    delete_coverage_files(dir_path=dir_path_git)
    exe_path = fuzz_compile(dir_path=dir_path_git, exec_name="grammar_fuzzer")
    grammar_fuzzer = Grammar_Fuzzer(
        grammar=SIMPLE_ABC_GRAMMAR, dir_path=seed_path, start_sym=START_SYMBOL
    )
    runner_fuzzing_grammar = ProgramRunner(program=exe_path)
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        result, outcome, grammar_seed = grammar_fuzzer.run(
            runner=runner_fuzzing_grammar
        )
    logger = Logger(fuzzer=grammar_fuzzer, runner=runner_fuzzing_grammar)
    logger.plot(path=os.path.abspath(os.path.join(seed_path, os.pardir)))
