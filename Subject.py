from enum import Enum


class Subject(Enum):
    """Класс - перечислитель констант школьных предметов, унаследован от Enum"""
    MATH = 'Математика'
    RUSSIAN_LANG = 'Русcкий Язык'
    FOREAN_LANG = 'Английский Язык'
    PHISICS = "Физика"
    GEOGRAPHY = "География"
    BIOLOGY = "Биология"
    HISTORY = "История"
    CHEMISTRY = "Химия"
