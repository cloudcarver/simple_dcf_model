from util import retrieve_from
 
# 3b732d31142b79d4e8d659612f55181a
class API_Data:
    def __init__(self, ticker, apikey='2bd6ce6f77da18e51c3e254ed9060702', url='https://financialmodelingprep.com', verbose=True):
        self.url = url
        self.ticker = ticker
        self.verbose = verbose
        self.say('Initiate data module...')
        self.profile = retrieve_from('{}/api/v3/profile/{}?apikey={}'.format(url, ticker, apikey))
        print('Rerieving data of {} From {}'.format(self.profile[0]['companyName'], url))
        self.say('Loading Income statements...')
        self.income_statements = retrieve_from('{}/api/v3/income-statement/{}?apikey={}'.format(url, ticker, apikey))
        self.say('Loading Balance Sheet...')
        self.balance_sheets = retrieve_from('{}/api/v3/balance-sheet-statement/{}?apikey={}'.format(url, ticker, apikey))
        self.say('Loading Statements of Cash Flow...')
        self.statements_of_cash_flow = retrieve_from('{}/api/v3/cash-flow-statement/{}?apikey={}'.format(url, ticker, apikey))
        self.say('Loading Quote...')
        self.quote = retrieve_from('{}/api/v3/quote/{}?apikey={}'.format(url, ticker, apikey))

    def net_receivable(self, period=0):
        return self.balance_sheets[period]['netReceivables']
    
    def account_payable(self, period=0):
        return self.balance_sheets[period]['accountPayables']

    def inventory(self, period=0):
        return self.balance_sheets[period]['inventory']

    def revenue(self, period=0):
        return self.income_statements[period]['revenue']

    def gross_profit_ratio(self, period=0):
        return self.income_statements[period]['grossProfitRatio']

    def operating_cash_flow(self, period=0):
        return self.statements_of_cash_flow[period]['operatingCashFlow']

    def total_liabilities(self, period=0):
        return self.balance_sheets[period]['totalLiabilities']

    def ebitda(self, period=0):
        return self.income_statements[period]['ebitda']

    def depreciation_and_amortization(self, period=0):
        return self.statements_of_cash_flow[period]['depreciationAndAmortization']
    
    def working_capital(self, period=0):
        return self.balance_sheets[period]['totalCurrentAssets'] - self.balance_sheets[period]['totalCurrentLiabilities']

    def capital_expenditure(self, period=0):
        return self.statements_of_cash_flow[period]['capitalExpenditure']

    def cash_and_cash_equivalent(self, period=0):
        return self.balance_sheets[period]['cashAndCashEquivalents']

    def stock_price(self, period=0):
        return self.quote[0]['price']

    @property
    def company_name(self):
        return self.profile[0]['companyName']
    
    @property
    def beta(self):
        return self.profile[0]['beta']

    @property
    def share_outstanding(self):
        return self.quote[0]['sharesOutstanding']

    @property
    def tax_rate(self):
        period = 0
        while self.income_statements[period]['incomeTaxExpense'] < 0:
            period = period + 1
        return self.income_statements[period]['incomeTaxExpense'] / self.income_statements[period]['incomeBeforeTax']

    def say(self, contet):
        if self.verbose:
            print('[DATA MODULE] {}'.format(contet))

if __name__ == "__main__":
    data = API_Data('F')
    print(data.net_receivable(1))