from sympy import im
from fuzzification import fuzzify
from inference import infer
from defuzzification import defuzzify

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        temp = fuzzify(input_dict)
        temp2 = infer(temp)
        return defuzzify(temp2)
