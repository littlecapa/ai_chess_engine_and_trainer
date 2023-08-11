from math import log10, copysign
EVAL_LIMIT = 15.0
EVAL_FACTOR = 100.0
MATE_STEP = 1
MIN_FORCED_MATE = 25
# 50 Moves means 100 Halfmoves
MAX_MATE_STEPS = 100
MATE_IN_ONE_VALUE = MIN_FORCED_MATE + MAX_MATE_STEPS * MATE_STEP
IS_MATE = 2 * MATE_IN_ONE_VALUE
import logging

def format_value(value):
    return round(float(value) * EVAL_FACTOR, 2)

def get_sign_abs(value):
     return copysign(1, value), abs(value)
     
def no_value(value):
    if value == 0 or value == "" or value == None:
        return True
    return False

def get_high_eval_add(abs_eval):
    return log10(abs_eval +1 - EVAL_LIMIT)
       
def get_mate_eval(mate):
    logging.info(f"Mate in: {mate}")
    sign_mate, abs_mate = get_sign_abs(mate)
    if abs(mate) == 1:
        return sign_mate * IS_MATE
    elif abs(mate) == 2:
        return sign_mate * MATE_IN_ONE_VALUE
    abs_mate -= 1
    abs_mate = min(MAX_MATE_STEPS, abs_mate)
    mate_eval = MIN_FORCED_MATE + (MAX_MATE_STEPS-abs_mate) * MATE_STEP
    return sign_mate * mate_eval
                 
def get_eval_eval(eval):
    sign_eval, abs_eval = get_sign_abs(eval)
    logging.debug(f"Eval: {eval} {sign_eval} {abs_eval}")
    if abs_eval <= EVAL_LIMIT:
        return eval
    else:
        return (EVAL_LIMIT + get_high_eval_add(abs_eval)) * sign_eval
                
def get_evaluation(eval, mate):
    if no_value(eval) and no_value(mate):
        return 0.0
    if no_value(mate):
        return format_value(get_eval_eval(eval))
    else:
        return format_value(get_mate_eval(mate))

def is_forced_mate(eval):
    return abs(eval) >= format_value(MIN_FORCED_MATE)

def is_mate(eval):
    return abs(eval) >= format_value(MATE_IN_ONE_VALUE)

def get_is_mate_value():
    return IS_MATE * EVAL_FACTOR

def get_mate_in_one_value():
    return MATE_IN_ONE_VALUE * EVAL_FACTOR
