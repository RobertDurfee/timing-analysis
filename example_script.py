import password_timing_analysis
from timeit import default_timer as timer

COMPARE_TYPE = 'SLOW'
PW = "SuPerDupeRStrongPassw0rd"

# Dummy string compare function
def str_compare_slow(str1, str2):

    i = 0

    while i < len(str1) and i < len(str2):

        if str1[i] != str2[i]:
            return

        i += 1

def str_compare_fast(str1, str2):
    return str1 == str2

str_compare = str_compare_slow if COMPARE_TYPE == 'SLOW' else str_compare_fast

# This query function must be implemented by the user and provided to Timea constructor.
def example_queryf(candidate):
    t1 = timer()
    str_compare(candidate, PW)
    t2 = timer()
    return (t2 - t1) * 10**7

# Create Timea object - provice timing query function and length of password (when to stop).
timea = password_timing_analysis.Timea(example_queryf, len(PW), decision_metric="gmm", decision_rule="max", queries=500)

timea.run()