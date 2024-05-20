from typing import Callable
import re


def generator_numbers(input_text: str) -> float:
    regex = r"\s(\d+\.\d+)\s"
    for i in re.finditer(regex, input_text, re.MULTILINE):
        yield float(i.group(1))


def sum_profit(input_text: str, func: Callable):
    return sum([i for i in func(input_text)])


text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'
total_income = sum_profit(text, generator_numbers)
print(f'Загальний дохід: {total_income}')
