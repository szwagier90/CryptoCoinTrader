import math

def exponentialMovingAverage(numbers, period):
    EMA = []
    for i in range(period-1):
        EMA.append(0)

    first_avg = sum(numbers[:period]) / period
    EMA.append(first_avg)

    alpha = 2 / float(1 + period)
    for num in numbers[period:]:
        currentEMA = ((num - EMA[-1]) * alpha) + EMA[-1]
        EMA.append(currentEMA)
        
    return EMA

def getMACD(numbers, slow=26, fast=12, signal=9):
    fast_ema = exponentialMovingAverage(numbers, fast)
    slow_ema = exponentialMovingAverage(numbers, slow)
    macd_line = [fast - slow for fast, slow in zip(fast_ema, slow_ema)]
    signal_line = exponentialMovingAverage(macd_line, signal)
    return macd_line, signal_line