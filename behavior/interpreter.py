# coding: utf-8

"""
Интерпретатор (Interpreter) - паттерн поведения классов.

Для заданного языка определяет представление его грамматики,
а также интерпретатор предложений этого языка.
"""


class RomanNumeralInterpreter(object):
    """Интерпретатор римских цифр"""
    def __init__(self):
        self.grammar = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def interpret(self, text):
        numbers = map(self.grammar.get, text)  # строки в значения
        if None in numbers:
            raise ValueError('Ошибочное значение: %s' % text)
        result = 0  # накапливаем результат
        temp = None  # запоминаем последнее значение
        while numbers:
            num = numbers.pop(0)
            if temp is None or temp >= num:
                result += num
            else:
                result += (num - temp * 2)
            temp = num
        return result

    def interpret2(self, text):
        n = [self.grammar.get(s) for s in text]  # Вариант с map был "стройнее"
        if None in n:
            raise ValueError('Ошибочное значение: %s' % text)
        result = 0  # Но сейчас обошлись без переменной temp...
        for i in range(len(n)):  # ... и без изменения списка
            if i == 0 or n[i - 1] >= n[i]:
                result += n[i]
            else:
                result += (n[i] - n[i - 1] * 2)
        return result


interp = RomanNumeralInterpreter()
print("Вариант 1")
print interp.interpret('MMMCMXCIX') == 3999  # True
print interp.interpret('MCMLXXXVIII') == 1988  # True
print("Вариант 2")
print interp.interpret2('MMMCMXCIX') == 3999  # True
print interp.interpret2('MCMLXXXVIII') == 1988  # True
