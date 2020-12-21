from urllib.request import urlopen
import json

def retrieve_from(url):
    response = urlopen(url)
    return json.loads(response.read().decode('utf-8'))

class Financial_calculator:
    @staticmethod
    def pv(cash, year_from_now, rate):
        return cash/((1 + rate)**year_from_now)

    @staticmethod
    def pv_of_cash_flows(cash_flows, rate):
        return sum([Financial_calculator.pv(cash, year + 1, rate) for year, cash in enumerate(cash_flows)])
        
    @staticmethod
    def pv_of_growing_perpetuity(cash, year_from_now, growing_rate, discount_rate):
        return (cash * (1 + growing_rate) / (discount_rate - growing_rate)) / ((1 + discount_rate)**year_from_now)

class Two_Stage_FCF_Model:
    def __init__(self, risk_free_rate, levered_beta, equity_risk_premium, levered_free_cash_flows, share_outstanding):
        self.risk_free_rate = risk_free_rate
        self.levered_beta = levered_beta
        self.equity_risk_premium = equity_risk_premium
        self.levered_free_cash_flows = levered_free_cash_flows
        self.share_outstanding = share_outstanding
    
    def get_discount_rate(self):
        return self.risk_free_rate + (self.levered_beta * self.equity_risk_premium)

    def get_total_equity_value(self):
        discount_rate = self.get_discount_rate()
        terminal_value = Financial_calculator.pv_of_growing_perpetuity(self.levered_free_cash_flows[-1], year_from_now=10, growing_rate=self.risk_free_rate, discount_rate=discount_rate)
        pv_of_levered_free_cash_flows = Financial_calculator.pv_of_cash_flows(self.levered_free_cash_flows, discount_rate)
        return terminal_value + pv_of_levered_free_cash_flows

    def get_value_per_share(self):
        return self.get_total_equity_value() / self.share_outstanding