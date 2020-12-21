import matplotlib.pyplot as plt
import numpy as np
from model import *
from data import API_Data
#
# Equity premium S&P Global https://www.spglobal.com/spdji/en/indices/strategy/sp-us-equity-risk-premium-index/#overview
# Ford levered beta https://www.infrontanalytics.com/fe-en/30019NU/Ford-Motor-Company/Beta 
# Geely levered beta https://www.infrontanalytics.com/fe-en/30019NU/Ford-Motor-Company/Beta 
# US risk free rate https://tradingeconomics.com/united-states/government-bond-yield
# CNHK risk free rate https://tradingeconomics.com/hong-kong/government-bond-yield
#
def analysis_script(title, current_stock_price, period, debt, share_outstanding, ebitda, depr_amort, changes_working_capital, cap_ex,
                    discount_rate, cap_ex_growth_rate, risk_free_rate, tax_rate, cash_and_cash_eq, plot=True):
    DCF = DCF_Model(debt, share_outstanding, period, ebitda,depr_amort,changes_working_capital,
                    cap_ex,discount_rate, 0, cap_ex_growth_rate,risk_free_rate,tax_rate, cash_and_cash_eq)
    earning_growth_rate_tests = np.linspace(0, 0.3, 100)
    equity_per_share_results = []
    break_even_earning_rate = None
    for e in earning_growth_rate_tests:
        DCF.earnings_growth_rate = e
        equity_value = DCF.get_equity_value()
        if break_even_earning_rate is None and equity_value > current_stock_price:
            break_even_earning_rate = e
        equity_per_share_results.append(equity_value)
    # print('break-even earning rate: {}'.format(break_even_earning_rate))
    if plot:
        plt.title("{} - {} years growing".format(title, period))
        plt.ylabel('Price/Value')
        plt.xlabel('Earning growth rate')
        plt.plot([0, 0.3], [current_stock_price, current_stock_price], label="{} stock price".format(title))
        plt.plot(earning_growth_rate_tests, equity_per_share_results, label="{} equity per share".format(title))
        plt.legend()
    return break_even_earning_rate

def dcf(ticker, period=5, risk_free_rate=0.0095, risk_premium=0.064):
    data = API_Data(ticker, verbose=True)
    print('title{} - {} years growing\n'.format(data.company_name, period), 
                    'current stock price {}\n'.format(data.stock_price()),
                    'period {}\n'.format(period),
                    'debt {}\n'.format(data.total_liabilities()),
                    'share_outstanding {}\n'.format(data.share_outstanding),
                    'ebitda {}\n'.format(data.ebitda()),
                    'depr_amort {}\n'.format(data.depreciation_and_amortization()),
                    'changes_working_capital {}\n'.format(data.working_capital(0) - data.working_capital(1)),
                    'cap_ex {}\n'.format(-1 * data.capital_expenditure()),
                    'discount_rate {}\n'.format(risk_free_rate + data.beta * risk_premium),
                    'cap_ex_growth_rate {}\n'.format(0.045),
                    'risk_free_rate {}\n'.format(risk_free_rate),
                    'tax_rate {}\n'.format(data.tax_rate),
                    'cash_and_cash_eq {}\n'.format(data.cash_and_cash_equivalent()))
    # https://financialmodelingprep.com/financial-statements/F
    return analysis_script(title=data.company_name, 
                    current_stock_price=data.stock_price(),
                    period=period,
                    debt=data.total_liabilities(),
                    share_outstanding=data.share_outstanding,
                    ebitda=data.ebitda(),
                    depr_amort=data.depreciation_and_amortization(),
                    changes_working_capital=data.working_capital(0) - data.working_capital(1),
                    cap_ex=-1 * data.capital_expenditure(),
                    discount_rate=risk_free_rate + data.beta * risk_premium, # risk_free_rate + (levered_beta * equity_risk_premium) 
                    cap_ex_growth_rate=0.045,
                    risk_free_rate=risk_free_rate, # https://tradingeconomics.com/united-states/government-bond-yield
                    tax_rate=data.tax_rate,
                    cash_and_cash_eq=data.cash_and_cash_equivalent())
    
if __name__ == "__main__":
    # dcf('TSLA', period=5)
    dcf('F', period=5)
    plt.show()


