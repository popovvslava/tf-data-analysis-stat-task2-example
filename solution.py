import pandas as pd
import scipy as sc
import numpy as np

from scipy.stats import norm


chat_id = 368379249  # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = (1 - p) / 2
    x = np.power(x, 2)
    sum_arr = sum(x)
    chi_low = sc.stats.chi2.ppf(1 - alpha, 2 * len(x))
    chi_up = sc.stats.chi2.ppf(alpha, 2 * len(x))
    low = np.sqrt(sum_arr / chi_low / 25)
    up = np.sqrt(sum_arr / chi_up / 25)
    return low, up
