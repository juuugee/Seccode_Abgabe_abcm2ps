import matplotlib.pyplot as plt
import os
import numpy as np
import pickle


class Logger:
    def __init__(self, fuzzer, runner):
        self.fuzzer = fuzzer
        self.runner = runner
        self.line_coverage = []
        self.branch_coverage = []
        self.call_coverage = []
        self.crash_amount = 0
        self.passes_amount = 0
        self.unresolves_amount = 0
        self.failed_seeds = []
        self.crashes = []
        self.unresolved = []
        self.passes = []
        self.get_information()

    def get_information(self):
        self.line_coverage = self.runner.return_line_coverage()
        self.branch_coverage = self.runner.return_branch_coverage()
        self.call_coverage = self.runner.return_call_coverage()
        self.crashes = self.runner.return_crashes()
        self.unresolved = self.runner.return_unresolved()
        self.passes = self.runner.return_passes()
        self.exec_per_sec = len(self.call_coverage) / (30 * 60)
        self.timestamp = self.runner.return_timestamp()
        self.start_timestamp = self.timestamp[0]
        (
            self.passes_amount,
            self.crash_amount,
            self.unresolves_amount,
        ) = self.runner.return_outcomes()
        self.failed_seeds = self.runner.return_failed_seeds()
        self.config_timestamp()

    def config_timestamp(self):
        for i in range(len(self.timestamp)):
            self.timestamp[i] = (self.timestamp[i] - self.start_timestamp) / (60)

    def plot(self, path):
        path_outcome = os.path.join(path, "outcome.svg")
        path_infos = os.path.join(path, "info.txt")
        path_failed_seeds = os.path.join(path, "failed_seeds.txt")
        path_line_cov = os.path.join(path, "line_coverage.svg")
        path_branch_cov = os.path.join(path, "branch_coverage.svg")
        path_statement_cov = os.path.join(path, "statement_coverage.svg")
        path_overall_cov = os.path.join(path, "overall_coverage.svg")
        path_crashes = os.path.join(path, "crashes.svg")
        with open(path_failed_seeds, "wb") as fp:
            pickle.dump(self.failed_seeds, fp)
        infostring = (
            "Exec: "
            + str(len(self.branch_coverage))
            + "\n"
            + "Exec per sec: "
            + str(self.exec_per_sec)
            + "\n"
            + "Passes: "
            + str(self.passes_amount)
            + "\n"
            + "Fails: "
            + str(self.crash_amount)
            + "\n"
            + "Unresolved: "
            + str(self.unresolves_amount)
        )
        with open(path_infos, "w") as f:
            f.write(infostring)
        plt.figure()
        plt.ylabel("Line Coverage in %")
        plt.xlabel("Zeit in min")
        plt.axis([0, 30, 0, 100])
        plt.plot(self.timestamp, self.line_coverage)
        plt.legend(["Line Coverage"])
        plt.savefig(path_line_cov, format="svg")
        plt.clf()
        plt.figure()
        plt.ylabel("Branch Coverage in %")
        plt.xlabel("Zeit in min")
        plt.axis([0, 30, 0, 100])
        plt.plot(self.timestamp, self.branch_coverage)
        plt.legend(["Branch Coverage"])
        plt.savefig(path_branch_cov, format="svg")
        plt.clf()
        plt.figure()
        plt.ylabel("Statement Coverage in %")
        plt.xlabel("Zeit in min")
        plt.axis([0, 30, 0, 100])
        plt.plot(self.timestamp, self.call_coverage)
        plt.legend(["Statement Coverage"])
        plt.savefig(path_statement_cov, format="svg")
        plt.clf()
        plt.figure()
        plt.ylabel("Coverages in %")
        plt.xlabel("Zeit in min")
        plt.axis([0, 30, 0, 100])
        plt.plot(self.timestamp, self.line_coverage)
        plt.plot(self.timestamp, self.branch_coverage)
        plt.plot(self.timestamp, self.call_coverage)
        plt.legend(["Line Coverages", "Branch Coverage", "Statement Coverage"])
        plt.savefig(path_overall_cov, format="svg")
        plt.clf()
        if max(self.crashes) > 0:
            plt.figure()
            plt.ylabel("Anazahl an Crashes")
            plt.xlabel("Zeit in min")
            plt.axis([0, 30, 0, max(self.crashes)])
            plt.plot(self.timestamp, self.crashes)
            plt.legend(["Crashes"])
            plt.savefig(path_crashes, format="svg")
            plt.clf()
        plt.clf()
        plt.figure()
        plt.ylabel("Anzahl an Ausführungen")
        plt.xlabel("Zeit in min")
        plt.axis(
            [
                0,
                30,
                0,
                (max(self.crash_amount, self.unresolves_amount, self.passes_amount)),
            ]
        )
        plt.plot(self.timestamp, self.crashes)
        plt.plot(self.timestamp, self.unresolved)
        plt.plot(self.timestamp, self.passes)
        plt.legend(["Fail", "Unresolved", "Pass"])
        plt.savefig(path_outcome, format="svg")
        plt.clf()
