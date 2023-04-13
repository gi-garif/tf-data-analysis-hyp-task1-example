import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 33217853 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.07
    
    control_success_rate = x_success / x_cnt
    test_success_rate = y_success / y_cnt
    success_rate = (x_success+y_success) / (x_cnt + y_cnt)
    
    SE = ((success_rate*(1-success_rate))/x_cnt + (success_rate*(1-success_rate))/y_cnt)**0.5
    
    z = (control_success_rate - test_success_rate) / SE
    
    p_value = norm.sf(abs(z)) * 2
    
    if p_value < alpha:
      result = True  
    else:
      result = False
    
    return result 

  
  
