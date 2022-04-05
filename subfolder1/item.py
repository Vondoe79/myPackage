from subfolder1.subfolder2.user import Employee


class Developer(Employee):
    raise_amount = 1.08

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

