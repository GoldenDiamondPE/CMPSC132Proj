class Date():
    def __init__(self, mm, dd, yyyy):
        self.mm = mm
        self.dd = dd
        self.yyyy = yyyy

    def set_mm(self, mm):
        self.mm = mm

    def set_dd(self, dd):
        self.dd = dd

    def set_yyyy(self, yyyy):
        self.yyyy = yyyy

    def get_mm(self):
        return self.mm

    def get_dd(self):
        return self.dd

    def get_yyyy(self):
        return self.yyyy

    def __str__(self):
        return f"{self.mm}-{self.dd}-{self.yyyy}"