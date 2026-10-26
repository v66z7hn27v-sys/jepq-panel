"""JEPQ dağıtım ve son kapanış verisini Yahoo Finance'ten çekip data/distributions.json dosyasını günceller.
Mevcut kayıtlar korunur; yalnızca yeni dağıtımlar eklenir. Ödeme tarihi Yahoo'da olmadığı için
yeni kayıtlarda hak kesim tarihinden 2 iş günü sonrası tahmin olarak yazılır."""
import json
import pathlib
from datetime import date, timedelta

import yfinance as yf

PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "distributions.json"


def add_business_days(d, n):
    while n > 0:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    known = {x["ex"] for x in data["distributions"]}

    t = yf.Ticker("JEPQ")
    divs = t.dividends
    for ts, amount in divs.items():
        ex = ts.date()
        if ex.isoformat() in known or ex < date(2025, 1, 1):
            continue
        data["distributions"].append({
            "ex": ex.isoformat(),
            "pay": add_business_days(ex, 2).isoformat(),
            "amount": round(float(amount), 5),
        })

    hist = t.history(period="5d")
    if not hist.empty:
        data["lastClose"] = round(float(hist["Close"].iloc[-1]), 2)
        data["lastCloseDate"] = hist.index[-1].date().isoformat()

    data["distributions"].sort(key=lambda x: x["ex"])
    data["updated"] = date.today().isoformat()
    PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
