py_library(
    # The name of the rule
    name = "math",
    # What files does this library use
    srcs = ["math.py"],
    # Mark this rule as public to allow other rules outside of this folder to depend on it
    visibility = ["//visibility:public"]
)

py_test(
    # The name of the test
    name = "math_test",
    # File of the unit test
    srcs = ["math_test.py"],
    # Dependencies
    deps = [":math"]
)
