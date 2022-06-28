'''
    In defuzzification step we deffizify the fuzzy set we receive from inference step.
    We use centroid method for defuzzification and we first use get_sth_set functions to get defiend output membership functions.
    Then in combine_output_sets we use inference output and it's membership values to limit those membership functions.
    Then we calculate the maximum of all of the functions and then calculate centroid using skfuzzy library.
    In defuzzify function we create the desired output string and return it.
'''
import numpy as np
import skfuzzy as skf
import matplotlib.pyplot as plt

def defuzzify(output_set: set):
    b, s = combine_output_sets(output_set)
    # plt.plot(b, s)
    # plt.show()
    output = skf.defuzz(b, s, 'centroid')
    outstr = ""
    if output < 1.78:
        outstr += "healthy & "
    if output >= 1 and output <= 2.51:
        outstr += "sick1 & "
    if output >= 1.78 and output <= 3.25:
        outstr += "sick2 & "
    if output >= 1.5 and output <= 4.5:
        outstr += "sick3 & "
    if output > 3.25:
        outstr += "sick4 & "
    if outstr == "":
        return None
    outstr = outstr[:-2] + f': {output}'
    return outstr

def combine_output_sets(output_set: set):
    start = 0
    end = 4.01
    step = 0.01
    steps = 401
    base = np.arange(start, end, step=step)
    output = np.zeros(steps)

    for key in output_set:
        cut_value = output_set[key]
        target_set = globals()[f'get_{key}_set'](base)
        cut_set = get_cut(target_set, cut_value)
        output = np.maximum(output, cut_set)

    return base, output

def get_healthy_set(base: list):
    return np.piecewise(base, [base <= 0.25, (base > 0.25) & (base <= 1), base > 1], [1, lambda x: 1 - (x - 0.25) / (1 - 0.25), 0])

def get_sick_1_set(base: list):
    return np.piecewise(base, [base <= 1, (base > 1) & (base <= 2), base > 2], [lambda x: (x - 0) / (1 - 0), lambda x: 1 - (x - 1) / (2 - 1), 0])

def get_sick_2_set(base: list):
    return np.piecewise(base, [base <= 1, (base > 1) & (base <= 2), (base > 2) & (base <= 3), base > 3], [0, lambda x: (x - 1) / (2 - 1), lambda x: 1 - (x - 2) / (3 - 2), 0])

def get_sick_3_set(base: list):
    return np.piecewise(base, [base <= 2, (base > 2) & (base <= 3), (base > 3) & (base <= 4), base > 4], [0, lambda x: (x - 2) / (3 - 2), lambda x: 1 - (x - 3) / (4 - 3), 0])

def get_sick_4_set(base: list):
    return np.piecewise(base, [base <= 3, (base > 3) & (base <= 3.75), base > 3.75], [0, lambda x: (x - 3) / (3.75 - 3), 1])

def get_cut(input: list, cut: float) -> list:
    return [min(x, cut) for x in input]

