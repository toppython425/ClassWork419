CREATE TABLE IF NOT EXISTS currencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS exchange_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (currency_id) REFERENCES currencies(id),
    UNIQUE (currency_id, date)
);


CREATE INDEX IF NOT EXISTS idx_currency_code ON currencies(code);
CREATE INDEX IF NOT EXISTS idx_rate_date ON exchange_rates(date);
CREATE INDEX IF NOT EXISTS idx_rate_currency ON exchange_rates(currency_id);