from vaulation import analysis_script
import matplotlib.pyplot as plt

def ford_dcf(period=5):
    # https://financialmodelingprep.com/financial-statements/F
    analysis_script(title="Ford - {} years growing".format(period), 
                    current_stock_price=9.15,
                    period=period,
                    debt=255307,
                    share_outstanding=3910,
                    ebitda=14326,
                    depr_amort=9689,
                    changes_working_capital=3165,
                    cap_ex=7632,
                    discount_rate=0.1055, # risk_free_rate + (levered_beta * equity_risk_premium) 
                    cap_ex_growth_rate=0.045,
                    risk_free_rate=0.0095, # https://tradingeconomics.com/united-states/government-bond-yield
                    tax_rate=0.15,
                    cash_and_cash_eq=17504)
    
def geely_dcf(period=5):
    analysis_script(title="Geely - {} years growing".format(period), 
                    current_stock_price=22.85,
                    debt=53003, 
                    share_outstanding=9820,
                    period=period,
                    ebitda=13497, # Net income + interest + taxes + depreciation + amortization 
                    depr_amort=3733,
                    changes_working_capital=513, 
                    cap_ex=2873,
                    discount_rate=0.1184, # risk_free_rate + (levered_beta * equity_risk_premium)
                    cap_ex_growth_rate=0.045,
                    risk_free_rate=0.00771,
                    tax_rate=0.121,
                    cash_and_cash_eq=20174)

def alibaba_dcf(period=5):
    analysis_script(title="Alibaba - {} years growing".format(period), 
                    current_stock_price=255.11,
                    debt=147287, 
                    share_outstanding=2706,
                    period=period,
                    ebitda=211604, 
                    depr_amort=42427,
                    changes_working_capital=158447, 
                    cap_ex=45386,
                    discount_rate=0.03318, # risk_free_rate + (levered_beta * equity_risk_premium)
                    cap_ex_growth_rate=0.045,
                    risk_free_rate=0.0095,
                    tax_rate=0.1277,
                    cash_and_cash_eq=330503)

def tsla_dcf(period=5):
    analysis_script(title="Tesla - {} years growing".format(period),
                    current_stock_price=633.25,
                    debt=13419, 
                    share_outstanding=948,
                    period=period,
                    ebitda=2087, 
                    depr_amort=2154,
                    changes_working_capital=3122, 
                    cap_ex=-1437,
                    discount_rate=0.15, # risk_free_rate + (levered_beta * equity_risk_premium)
                    cap_ex_growth_rate=0.045,
                    risk_free_rate=0.0095,
                    tax_rate=0.1277,
                    cash_and_cash_eq=6268)

def bmw_dcf(period=5):
    analysis_script(title="BMW - {} years growing".format(period), 
                    current_stock_price=74.83,
                    debt=98660, 
                    share_outstanding=602,
                    period=period,
                    ebitda=13947, 
                    depr_amort=6017,
                    changes_working_capital=-4624, 
                    cap_ex=6902,
                    discount_rate=0.0818, # risk_free_rate + (levered_beta * equity_risk_premium)
                    cap_ex_growth_rate=0.045,
                    risk_free_rate=0.0095,
                    tax_rate=0.300,
                    cash_and_cash_eq=9961)

def tm_dcf(period=5):
    analysis_script(title="Toyota - {} years growing".format(period), 
                    current_stock_price=152.85,
                    debt=1171549, 
                    share_outstanding=1400,
                    period=period,
                    ebitda=3786747, # Net income + interest + taxes + depreciation + amortization 
                    depr_amort=1605383,
                    changes_working_capital=87855, 
                    cap_ex=3595131,
                    discount_rate=0.05686, # risk_free_rate + (levered_beta * equity_risk_premium)
                    cap_ex_growth_rate=0.045,
                    risk_free_rate=0.0095,
                    tax_rate=0.2416,
                    cash_and_cash_eq=2774498)

def atnt_dcf(period=5):
    analysis_script(title="AT&T - {} years growing".format(period),
                    current_stock_price=30.58,
                    debt=367448, 
                    share_outstanding=7130,
                    period=period,
                    ebitda=54035, # Net income + interest + taxes + depreciation + amortization 
                    depr_amort=28217,
                    changes_working_capital=-1577, 
                    cap_ex=-19435,
                    discount_rate=0.06006, # risk_free_rate + (levered_beta * equity_risk_premium)
                    cap_ex_growth_rate=0.045,
                    risk_free_rate=0.0095,
                    tax_rate=0.1891,
                    cash_and_cash_eq=12130)

if __name__ == "__main__":
    ford_dcf(period=5)
    plt.show()
    geely_dcf(period=5)
    plt.show()