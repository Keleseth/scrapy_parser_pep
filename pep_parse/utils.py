import re

from pep_parse.exceptions import PatternMatchError


def extract_text_with_pattern(pattern, text):
    """
    Функция принимает регулярное выражение и строку,
    возвращая все группы из регулярного выражения.
    """
    print(text)
    matched_groups = re.search(pattern, text)
    if not matched_groups:
        raise PatternMatchError(text, pattern)
    return matched_groups.groups()
