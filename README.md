# JEPQ Paneli

JPMorgan Nasdaq Equity Premium Income ETF (JEPQ) için aylık dağıtım takibi, pasif gelir ve opsiyon getiri hesaplayıcısı.

**Canlı panel:** https://v66z7hn27v-sys.github.io/jepq-panel/

## İçerik
- Son kapanış, son dağıtım, son 12 ay dağıtım ve getiri
- TradingView grafiği (QQQ karşılaştırmalı)
- Aylık dağıtım grafiği ve geçmiş tablosu
- Pasif gelir hesaplayıcı (USD/TL, stopaj, DRIP)
- Covered call ve cash-secured put getiri hesaplayıcı

## Veri güncelleme
`.github/workflows/update-data.yml` hafta içi her gün ABD kapanışından sonra `scripts/update_data.py` ile `data/distributions.json` dosyasını Yahoo Finance verisiyle günceller. Elle çalıştırmak için: Actions → Veri güncelle → Run workflow.

Bilgilendirme amaçlıdır, yatırım tavsiyesi değildir.
