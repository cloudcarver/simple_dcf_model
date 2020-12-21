from util import Financial_calculator
class DCF_Model:
    def __init__(self, debt, share_outstanding, period, ebitda, depr_amort, changes_working_capital, 
    cap_ex, discount_rate, earnings_growth_rate, cap_ex_growth_rate, risk_free_rate, tax_rate, cash_and_cash_eq, verbose=False):
        self.period = period
        self.ebitda = ebitda
        self.depr_amort = depr_amort
        self.changes_working_capital = changes_working_capital
        self.cap_ex = cap_ex
        self.discounte_rate = discount_rate
        self.tax_rate = tax_rate
        self.earnings_growth_rate = earnings_growth_rate
        self.cap_ex_growth_rate = cap_ex_growth_rate
        self.risk_free_rate = risk_free_rate
        self.verbose = verbose
        self.debt = debt
        self.share_outstanding = share_outstanding
        self.cash_and_cash_eq = cash_and_cash_eq

    def get_enterprise_value(self):
        ebit = self.ebitda - self.depr_amort
        depr_amort = self.depr_amort
        cwc = self.changes_working_capital      
        cap_ex = self.cap_ex

        flows = []
        if self.verbose:
            print('Forecasting flows for {} years out.'.format(self.period), 
            ('\n         Cash   |    EBIT   |    D&A    |    CWC    |   CAP_EX  | '))
        for yr in range(1, self.period + 1):
            ebit = ebit * (1 + self.earnings_growth_rate)
            depr_amort = depr_amort * (1 + self.earnings_growth_rate)
            cwc = cwc * 0.7
            cap_ex = cap_ex * (1 + self.cap_ex_growth_rate)
            flow = ebit * (1 - self.tax_rate) + depr_amort - cwc - cap_ex
            flows.append(flow)
            if self.verbose:
                print(str(2019 + yr) + '  ','%.2E' % flow + ' | ','%.2E' % ebit + ' | ','%.2E' % depr_amort + ' | ','%.2E' % cwc + ' | ','%.2E' % cap_ex + ' | ')
        terminal_pv = Financial_calculator.pv_of_growing_perpetuity(flows[-1], 5, self.risk_free_rate, self.discounte_rate)
        enterprise_value = Financial_calculator.pv_of_cash_flows(flows, self.discounte_rate) + terminal_pv
        return enterprise_value
    
    def get_equity_value(self):
        return (self.get_enterprise_value() - self.debt + self.cash_and_cash_eq) / self.share_outstanding