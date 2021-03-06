# enable reporting of the result
REPORT_MODE = 0

#print everything in the console
PRINT_MODE = 0

# enable log file to print all exception
DEBUG_MODE = 0

# check false positive in concurrency
CHECK_CONCURRENCY_FP = 0

# Timeout for z3 in ms
TIMEOUT = 100

# Set this flag to 2 if we want to do evm real value unit test
# Set this flag to 3 if we want to do evm symbolic unit test
UNIT_TEST = 0

# timeout to run symbolic execution (in secs)
GLOBAL_TIMEOUT = 50

# timeout to run symbolic execution (in secs) for testing
GLOBAL_TIMEOUT_TEST = 2

# print path conditions
PRINT_PATHS = 0

# WEB = 1 means that we are using Oyente for web service
WEB = 1

# Redirect results to a json file.
STORE_RESULT = 0

# depth limit for DFS

DEPTH_LIMIT = 50

# # add by aq
# DEPTH_LIMIT = 1


GAS_LIMIT = 4000000

LOOP_LIMIT = 10

# Use a public blockchain to speed up the symbolic execution
USE_GLOBAL_BLOCKCHAIN = 1

USE_GLOBAL_STORAGE = 0

# Take state data from state.json to speed up the symbolic execution
INPUT_STATE = 1

# Check assertions
CHECK_ASSERTIONS = 0

GENERATE_TEST_CASES = 0

# Run Oyente in parallel
PARALLEL = 0
