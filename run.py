from grammar_guided_fuzzer.exp1_line_coverage.exp1 import (
    run_grammar_guided_line_coverage_fuzzer,
)
from grammar_guided_fuzzer.exp2_branch_coverage.exp2 import (
    run_grammar_guided_branch_coverage_fuzzer,
)
from grammar_guided_fuzzer.exp3_statement_coverage.exp3 import (
    run_grammar_guided_statement_coverage_fuzzer,
)
from guided_mutation_fuzzer.exp3_statement_coverage.exp3 import (
    run_mutation_coverage_fuzzer_statement_coverage,
)
import time

dir_path_git = "/pfs/data5/home/es/es_es/es_jugeit01/seccode_fuzzing/abcm2ps"
run_mutation_coverage_fuzzer_statement_coverage(
    run_time_in_min=30,
    dir_path_git=dir_path_git,
    seed_path="/pfs/data5/home/es/es_es/es_jugeit01/seccode_fuzzing/guided_mutation_fuzzer/exp3_statement_coverage/in",
)
print("done 1")
run_grammar_guided_line_coverage_fuzzer(
    run_time_in_min=30,
    dir_path_git=dir_path_git,
    seed_path="/pfs/data5//home/es/es_es/es_jugeit01/seccode_fuzzing/grammar_guided_fuzzer/exp1_line_coverage/in_mutated_grammar",
)
print("done 2")
run_grammar_guided_branch_coverage_fuzzer(
    run_time_in_min=30,
    dir_path_git=dir_path_git,
    seed_path="/pfs/data5//home/es/es_es/es_jugeit01/seccode_fuzzing/grammar_guided_fuzzer/exp2_branch_coverage/in_mutated_grammar",
)
print("done 3")
run_grammar_guided_statement_coverage_fuzzer(
    run_time_in_min=30,
    dir_path_git=dir_path_git,
    seed_path="/pfs/data5//home/es/es_es/es_jugeit01/seccode_fuzzing/grammar_guided_fuzzer/exp3_statement_coverage/in_mutated_grammar",
)
print("done 4")
