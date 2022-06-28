'''
    In inference.py we receive the output fuzzy set of fuzzification step
    and use the pre set rules to calculate output fuzzy set of the fuzzy system.
'''

''' this function returns rules in the rules.fcl file as a list of strings. '''
def get_rules():
    with open('./rules.fcl', "r") as f:
        contents = f.readlines()
    return contents

''' 
    this function splits the rule string and
    extracts more important parts of a rule including conditions, logical operator and result.
    output looks like {parameter1: fuzzyvalue1, ...}, {output: fuzzyvalue}, AND/OR
'''
def extract_rule(rule: str):
    clauses = []
    [_, __, s] = rule.partition(" IF ")
    [clause, _, result] = s.partition(" THEN ")
    if clause.find(" AND ") != -1:
        clauses = clause.split(" AND ")
        op = "AND"
    else:
        clauses = clause.split(" OR ")
        op = "OR"
    try:
        temp = [c[1:-1].split(" IS ") for c in clauses]
        cs = dict(temp)
        temp2 = [result[:-1].split(" IS ")]
        rs = dict(temp2)
    except Exception:
        print(f'rule {rule} has problem being interpreted!')
    return cs, rs, op

''' uses fuzzification result and the extracted form of a rule to calculate membership of the rule's output value if the rule contained OR operator. '''
def get_max(input: dict, clauses: dict):
    max = 0
    for key in clauses.keys():
        value = input[key][clauses[key]]
        if value > max:
            max = value
    return max

''' uses fuzzification result and the extracted form of a rule to calculate membership of the rule's output value if the rule contained AND operator. '''
def get_min(input: dict, clauses: dict):
    min = 1
    for key in clauses.keys():
        value = input[key][clauses[key]]
        if value < min:
            min = value
    return min

''' 
    goes throgh all rules and computes maximum membership of each output fuzzy value using extract_rule,
    get_min and get_max functions.
    output of the function is the output fuzzy set we look to defuzzify in next step.
'''
def infer(input):
    result = {'healthy': 0, 'sick_1': 0, 'sick_2': 0, 'sick_3': 0, 'sick_4': 0}
    rules = get_rules()
    for rule in rules:
        rule = rule.strip()
        if rule == "":
            continue
        c, r, o = extract_rule(rule)
        if o == "AND":
            v = get_min(input, c)
        elif o == "OR":
            v = get_max(input, c)
        else:
            print(f"rule {rule} has wrong logical op!")
        if result.get(r["health"], 0) < v:
            result[r["health"]] = v
    return result
    