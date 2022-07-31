import subprocess
from fuzzingbook.Fuzzer import Runner
from fuzzing.fuzzing_coverage import call_gcov
import time


class ProgramRunner(Runner):
    def __init__(self, program):
        """Initialize.  `program` is a program spec as passed to `subprocess.run()`"""
        self.program_path = program
        self.coverages = []
        self.branch_coverage = []
        self.line_coverage = []
        self.statement_coverage = []
        self.crashes = 0
        self.crash_timestamp = []
        self.time_stamp = []
        self.crashes_array = []
        self.passes = 0
        self.unresolved = 0
        self.fail_seed_list = []
        self.passes_array = []
        self.unresolved_array = []

    def run_process(self, inp=""):
        """
        description: Run the program at specified programm_path with inputfile_path as `inp` as input with subprocess.run()

        input:
        inp(str): path to the input file

        output:
        subprocess
        """
        exec_array = [self.program_path, inp]
        return subprocess.run(
            exec_array,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

    def run(self, inp=""):
        """
        description: Run the program at specified programm_path with inputfile_path as `inp` as input with subprocess.run() and evalute subprocess.run()

        input:
        inp(str): path to the input file

        output:
        result: result of subprocess
        outcome: FAIL, PASS or UNRESOLVED
        """
        mutated_seed = inp[1]
        result = self.run_process(inp[0])

        if result.returncode == 0:
            outcome = self.PASS
            self.passes = self.passes + 1
        elif result.returncode < 0:
            outcome = self.FAIL
            self.crashes = self.crashes + 1
            self.fail_seed_list.append(mutated_seed)
        else:
            outcome = self.UNRESOLVED
            self.unresolved = self.unresolved + 1

        self.coverages = call_gcov(self.program_path)
        self.line_coverage.append(self.coverages[0])
        self.branch_coverage.append(self.coverages[1])
        self.statement_coverage.append(self.coverages[2])
        self.crashes_array.append(self.crashes)
        self.passes_array.append(self.passes)
        self.unresolved_array.append(self.unresolved)
        self.time_stamp.append(time.time())
        return (result, outcome, mutated_seed)

    def return_line_coverage(self):
        return self.line_coverage

    def return_branch_coverage(self):
        return self.branch_coverage

    def return_call_coverage(self):
        return self.statement_coverage

    def return_crashes(self):
        return self.crashes_array

    def return_passes(self):
        return self.passes_array

    def return_unresolved(self):
        return self.unresolved_array

    def return_timestamp(self):
        return self.time_stamp

    def return_outcomes(self):
        return self.passes, self.crashes, self.unresolved

    def return_failed_seeds(self):
        return self.fail_seed_list


class ProgrammCoverageRunner(ProgramRunner):
    def return_actual_line_coverage(self):
        return self.line_coverage[-1]

    def return_actual_branch_coverage(self):
        return self.branch_coverage[-1]

    def return_actual_statment_coverage(self):
        return self.statement_coverage[-1]
