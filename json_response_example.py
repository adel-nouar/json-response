import json
from yahoofinancials import YahooFinancials


def get_statement(ticker, frequency='quartely', statement='income'):
    yahoo_financials = YahooFinancials(ticker)
    return yahoo_financials.get_financial_stmts(frequency, statement)


my_ticker = 'AAPL'
income_statement = get_statement(my_ticker)

print(json.dumps(income_statement, indent=2))

income_statement = income_statement.get('incomeStatementHistoryQuarterly', {})
income_statement = income_statement.get(my_ticker, [])

for quarter in income_statement:
    for k, v in quarter.items():
        print(k, 'net income', v['netIncome'])
