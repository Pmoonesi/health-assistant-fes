'''
In fuzzification.py we receive the crisp input from the GUI in form of a set and convert it to a fuzzy set.
There are functions with names like get-sth-fuzzied wich will be used to get a fuzzy set out of every crisp input value.
All parameters except four have charts in project manual and are calculated according to those charts. The other four values are going to stay crisp but in form of fuzzy sets.
For the last step, we use fuzzify function to combine returned fuzzy sets of every get-sth-fuzzied function and return the combined set.
'''

import numpy as np

## we use this dictionary to convert gui returned set to the set we can use in inference step (matches the rules).
translate_dict = {
    "chest_pain": "chest_pain",
    "cholestrol": "cholesterol",
    "ecg": "ECG",
    "exercise": "exercise",
    "thallium_scan": "thallium",
    "age": "age",
    "blood_pressure": "blood_pressure",
    "blood_sugar": "blood_sugar",
    "heart_rate": "maximum_heart_rate",
    "old_peak": "old_peak",
    "sex": "sex"
}

def get_age_fuzzied(age: float):
    ## young
    young_membership = np.piecewise(age, [age <= 29, (age > 29 and age <= 38), age > 38], [1, lambda x: 1 - (x - 29) / (38 - 29), 0])

    ## mild
    mild_membership = np.piecewise(age, [age <= 33, (age > 33 and age <= 38), (age > 38 and age <= 45), age > 45], [0, lambda x: (x - 33) / (38 - 33), lambda x: 1 - (x - 38) / (45 - 38), 0])

    ## old
    old_membership = np.piecewise(age, [age <= 40, (age > 40 and age <= 48), (age > 48 and age <= 58), age > 58], [0, lambda x: (x - 40) / (48 - 40), lambda x: 1 - (x - 48) / (58 - 48), 0])

    ## very old
    veryold_membership = np.piecewise(age, [age <= 52, (age > 52 and age <= 60), age > 60], [0, lambda x: (x - 52) / (60 - 52), 1])

    ## combine
    s = [('young', young_membership), ('mild', mild_membership), ('old', old_membership), ('very_old', veryold_membership)]
    s = dict([(key, float(value)) for key, value in s])
    return s

def get_blood_pressure_fuzzied(bp: float):
    ## low
    low_membership = np.piecewise(bp, [bp <= 111, (bp > 111 and bp <= 134), bp > 134], [1, lambda x: 1 - (x - 111) / (134 - 111), 0])

    ## medium
    medium_membership = np.piecewise(bp, [bp <= 127, (bp > 127 and bp <= 139), (bp > 139 and bp <= 153), bp > 153], [0, lambda x: (x - 127) / (139 - 127), lambda x: 1 - (x - 139) / (153 - 139), 0])

    ## high
    high_membership = np.piecewise(bp , [bp <= 142, (bp > 142 and bp <= 157), (bp > 157 and bp <= 172), bp > 172], [0, lambda x: (x - 142) / (157 - 142), lambda x: 1 - (x - 157) / (172 - 157), 0])

    ## veryhigh
    veryhigh_membership = np.piecewise(bp, [bp <= 154, (bp > 154 and bp <= 171), bp > 171], [0, lambda x: (x - 154) / (171 - 154), 1])

    ## combine
    s = [('low', low_membership), ('medium', medium_membership), ('high', high_membership), ('very_high', veryhigh_membership)]
    s = dict([(key, float(value)) for key, value in s])
    return s

def get_blood_sugar_fuzzied(bs: float):
    ## veryhigh
    veryhigh_membership = np.piecewise(bs, [bs <= 105, (bs > 105 and bs <= 120), bs > 120], [0, lambda x: (x - 105) / (120 - 105), 1])

    s = [('true', veryhigh_membership), ('false', 1 - veryhigh_membership)]
    s = dict([(key, float(value)) for key, value in s])
    return s

def get_cholestrol_fuzzied(ch: float):
    ## low
    low_membership = np.piecewise(ch, [ch <= 151, (ch > 151 and ch <= 197), ch > 197], [1, lambda x: 1 - (x - 151) / (197 - 151), 0])

    ## medium
    medium_membership = np.piecewise(ch, [ch <= 188, (ch > 188 and ch <= 215), (ch > 215 and ch <= 250), ch > 250], [0, lambda x: (x - 188) / (215 - 188), lambda x: 1 - (x - 215) / (250 - 215), 0])

    ## high
    high_membership = np.piecewise(ch, [ch <= 217, (ch > 217 and ch <= 263), (ch > 263 and ch <= 307), ch > 307], [0, lambda x: (x - 217) / (263 - 217), lambda x: 1 - (x - 263) / (307 - 263), 0])

    ## veryhigh
    veryhigh_membership = np.piecewise(ch, [ch <= 281, (ch > 281 and ch <= 347), ch > 347], [0, lambda x: (x - 281) / (347 - 281), 1])

    ## combine
    s = [('low', low_membership), ('medium', medium_membership), ('high', high_membership), ('very_high', veryhigh_membership)]
    s = dict([(key, float(value)) for key, value in s])
    return s

def get_heart_rate_fuzzied(hr: float):
    ## low
    low_membership = np.piecewise(hr, [hr <= 100, (hr > 100 and hr <= 141), hr > 141], [1, lambda x: 1 - (x - 100) / (141 - 100), 0])

    ## medium
    medium_membership = np.piecewise(hr, [hr <= 111, (hr > 111 and hr <= 152), (hr > 152 and hr <= 194), hr > 194], [0, lambda x: (x - 111) / (152 - 111), lambda x: 1 - (x - 152) / (194 - 152), 0])

    ## high
    high_membership = np.piecewise(hr, [hr <= 152, (hr > 152 and hr <= 210), hr > 210], [0, lambda x: (x - 152) / (210 - 152), 1])

    ## combine 
    s = [('low', low_membership), ('medium', medium_membership), ('high', high_membership)]
    s = dict([(key, float(value)) for key, value in s])
    return s

def get_ecg_fuzzied(ecg: float):
    ## normal
    normal_membership = np.piecewise(ecg, [ecg <= 0, (ecg > 0 and ecg <= 0.4), ecg > 0.4], [1, lambda x: 1 - x / (0.4 - 0), 0])
    
    ## abnormal
    abnormal_membership = np.piecewise(ecg, [ecg <= 0.2, (ecg > 0.2 and ecg <= 1), (ecg > 1 and ecg <= 1.8), ecg > 1.8], [0, lambda x: (x - 0.2) / (1 - 0.2), lambda x: 1 - (x - 1) / (1.8 - 1), 0])

    ## hypertrophy
    hypertrophy_membership = np.piecewise(ecg, [ecg <= 1.4, (ecg > 1.4 and ecg <= 1.9), ecg > 1.9], [0, lambda x: (x - 1.4) / (1.9 - 1.4), 1])

    ## combine
    s = [('normal', normal_membership), ('abnormal', abnormal_membership), ('hypertrophy', hypertrophy_membership)]
    s = dict([(key, float(value)) for key, value in s])
    return s

def get_old_peak_fuzzied(op: float):
    ## low
    low_membership = np.piecewise(op, [op <= 1, (op > 1 and op <= 2), op > 2], [1, lambda x: 1 - (x - 1) / (2 - 1), 0])

    ## risk
    risk_membership = np.piecewise(op, [op <= 1.5, (op > 1.5 and op <= 2.8), (op > 2.8 and op <= 4.2), op > 4.2], [0, lambda x: (x - 1.5) / (2.8 - 1.5), lambda x: 1 - (x - 2.8) / (4.2 - 2.8), 0])

    ## terrible
    terrible_membership = np.piecewise(op, [op <= 2.5, (op > 2.5 and op <= 4), op > 4], [0, lambda x: (x - 2.5) / (4 - 2.5), 1])

    ## combine
    s = [('low', low_membership), ('risk', risk_membership), ('terrible', terrible_membership)]
    s = dict([(key, float(value)) for key, value in s])
    return s

def get_chest_pain_fuzzied(cp: float):
    s = []
    s.append(('typical_anginal', 1.0 if cp == 1 else 0.0))
    s.append(('atypical_anginal', 1.0 if cp == 2 else 0.0))
    s.append(('non_aginal_pain', 1.0 if cp == 3 else 0.0))
    s.append(('asymptomatic', 1.0 if cp == 4 else 0.0))
    return dict(s)

def get_exercise_fuzzied(ex: float):
    s = []
    s.append(('false', 1.0 if ex == 0 else 0.0))
    s.append(('true', 1.0 if ex == 1 else 0.0))
    return dict(s)

def get_thallium_scan_fuzzied(th: float):
    s = []
    s.append(('normal', 1.0 if th == 3 else 0.0))
    s.append(('medium', 1.0 if th == 6 else 0.0))
    s.append(('high', 1.0 if th == 7 else 0.0))
    return dict(s)

def get_sex_fuzzied(sx: float):
    s = []
    s.append(('male', 1.0 if sx == 0 else 0.0))
    s.append(('female', 1.0 if sx == 1 else 0.0))
    return dict(s)

def fuzzify(input_values: dict):
    input_arr = [(key, float(value)) for key, value in input_values.items()]
    f_input = dict(input_arr)
    result = {}
    for key in f_input.keys():
        result[translate_dict[key]] = globals()[f'get_{key}_fuzzied'](f_input[key])
    return result