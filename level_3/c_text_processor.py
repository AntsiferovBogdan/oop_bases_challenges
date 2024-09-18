"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""
from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True)
class TextProcessor:
    text: str

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'


@dataclass(frozen=True)
class AdvancedTextProcessor(TextProcessor):
    def summarize(self) -> str:
        return f'{super().summarize()}. Total number of words in the text: {len(self.text.split())}'


if __name__ == '__main__':
    processor = TextProcessor(text='This is Sparta')
    print(processor.to_upper())
    print(processor.summarize())

    advenced_processor = AdvancedTextProcessor(text='This is Sparta')
    print(advenced_processor.to_upper())
    print(advenced_processor.summarize())
