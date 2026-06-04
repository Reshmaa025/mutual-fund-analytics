# Mutual Fund Analytics Data Dictionary

## fact_nav
- amfi_code: Fund identifier
- date: NAV date
- nav: Net Asset Value

## fact_transactions
- investor_id: Unique investor
- transaction_type: SIP / Lumpsum / Redemption
- amount: Transaction value (>0)
- state: Investor location
- kyc_status: KYC verification status

## fact_performance
- 1Y_return: 1 year return %
- 3Y_return: 3 year return %
- 5Y_return: 5 year return %
- expense_ratio: Fund expense %

## fact_aum
- aum: Assets Under Management