# day32_basic_logic.py

import re
from collections import Counter

def cal_shipping_fee(weight):
    if not weight or weight > 20000 or weight == 0:
        return ValueError('무게는 20000g 이하입니다')
    result_fee = 3000 + (weight // 1000) * 1000
    return result_fee











































































