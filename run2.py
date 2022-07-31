from muation_fuzzer.exp1 import run_mutation_fuzzer
from grammar_based_fuzzer.exp1 import run_grammar_fuzzer
from guided_mutation_fuzzer.exp1_line_coverage.exp1 import (
    run_mutation_coverage_fuzzer_line_coverage,
)
from guided_mutation_fuzzer.exp2_branch_coverage.exp2 import (
    run_mutation_coverage_fuzzer_branch_coverage,
)
import time

dir_path_git = "/pfs/data5/home/es/es_es/es_jugeit01/seccode_fuzzing/abcm2ps"
# run_mutation_coverage_fuzzer_branch_coverage(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/pfs/data5/home/es/es_es/es_jugeit01/seccode_fuzzing/guided_mutation_fuzzer/exp2_branch_coverage/in")
# print("done 1")
# run_mutation_fuzzer(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/pfs/data5/home/es/es_es/es_jugeit01/seccode_fuzzing/muation_fuzzer/in")
# print("done 2")
run_mutation_coverage_fuzzer_line_coverage(
    run_time_in_min=30,
    dir_path_git=dir_path_git,
    seed_path="/pfs/data5/home/es/es_es/es_jugeit01/seccode_fuzzing/guided_mutation_fuzzer/exp1_line_coverage/in",
)
print("done 3")
run_grammar_fuzzer(
    run_time_in_min=30,
    dir_path_git=dir_path_git,
    seed_path="/pfs/data5/home/es/es_es/es_jugeit01/seccode_fuzzing/grammar_based_fuzzer/in",
)
print("done 4")
