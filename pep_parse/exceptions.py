class PatternMatchError(Exception):
    """
    Вызывается, когда строка не соответствует регулярному выражению.
    """

    def __init__(self, text, pattern):
        super().__init__(
            f'Строка "{text}" не соответствует регулярному выражению:'
            f'{pattern}'
        )
