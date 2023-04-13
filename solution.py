import pandas as pd
import numpy as np
from scipy import stats


chat_id = 973327975 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # рассчитываем доли успехов в выборках
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt

    # рассчитываем статистику теста
    t_statistic = (p2 - p1) / ( ((p1 * (1 - p1)) / x_cnt) + ((p2 * (1 - p2)) / y_cnt) )**0.5

    # рассчитываем критическое значение
    t_critical = stats.t.ppf(0.9, x_cnt + y_cnt - 2)

    # сравниваем статистику теста и критическое значение
    return t_statistic > t_critical
