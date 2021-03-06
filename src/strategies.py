import src.instruments as inst
import src.debt_portfolio as dpf

from calendar import monthrange
from datetime import date, timedelta, datetime

class IssuanceStrategy():
    def __init__(self):
        pass

    def get_issuance(self, issuance_date, amount, yield_curve):
        pass

class SingleBond(IssuanceStrategy):
    def __init__(self, ttm_of_bond):
        self.ttm = ttm_of_bond

    def get_issuance(self, issuance_date, amount, yield_curve):
        settle = issuance_date

        y = settle.year
        m = settle.month
        d = settle.day

        maturity = datetime(y, m, d) + timedelta(days = self.ttm*365)
        maturity = maturity.date()
        issuance_cost = 0 # Par bond
        coupon = yield_curve.get_yield(settle, self.ttm)
        symbol = f'{self.ttm} Bond {maturity}, {coupon*100:.2f} %'
        return [dpf.Position(inst.Bond(issuance_date, maturity, issuance_cost, coupon, symbol), amount)]
