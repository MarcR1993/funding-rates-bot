import requests
import time
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials
from config import *

class FundingRateCollector:
    def __init__(self):
        self.setup_google_sheets()
    
    def setup_google_sheets(self):
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        credentials = Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=scope
        )
        
        self.gc = gspread.authorize(credentials)
        self.sheet = self.gc.open_by_key(SHEET_ID)
        
        try:
            self.worksheet = self.sheet.worksheet("Funding Rates")
        except:
            self.worksheet = self.sheet.add_worksheet(
                title="Funding Rates", rows="1000", cols="10"
            )
        
        if len(self.worksheet.get_all_values()) == 0:
            headers = ['Timestamp', 'Date', 'Exchange', 'Symbol', 'Funding_Rate_%', 'Next_Funding_Time', 'Status']
            self.worksheet.append_row(headers)
        
        print("✅ Connexion Google Sheets établie")
    
    def get_binance_funding(self):
        try:
            url = "https://fapi.binance.com/fapi/v1/premiumIndex"
            response = requests.get(url, timeout=10)
            data = response.json()
            return [item for item in data if item['symbol'] in BINANCE_SYMBOLS]
        except Exception as e:
            print(f"❌ Erreur Binance: {e}")
            return []
    
    def get_kucoin_funding(self):
        try:
            results = []
            for symbol in KUCOIN_SYMBOLS:
                url = f"https://api-futures.kucoin.com/api/v1/funding-rate/{symbol}/current"
                response = requests.get(url, timeout=10)
                data = response.json()
                if data['code'] == '200000':
                    results.append({
                        'symbol': symbol,
                        'fundingRate': data['data']['value'],
                        'nextFundingTime': data['data']['timePoint']
                    })
                time.sleep(0.1)
            return results
        except Exception as e:
            print(f"❌ Erreur KuCoin: {e}")
            return []
    
    def save_data(self, binance_data, kucoin_data):
        rows = []
        timestamp = int(time.time())
        date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        for item in binance_data:
            rate = float(item['lastFundingRate']) * 100
            next_time = datetime.fromtimestamp(int(item['nextFundingTime'])/1000).strftime('%Y-%m-%d %H:%M:%S')
            status = "🔴 LONG PAY" if rate > 0.1 else "🟢 SHORT PAY" if rate < -0.1 else "🟡 NEUTRAL"
            rows.append([timestamp, date_str, 'Binance', item['symbol'], round(rate, 4), next_time, status])
        
        for item in kucoin_data:
            rate = float(item['fundingRate']) * 100
            next_time = datetime.fromtimestamp(int(item['nextFundingTime'])/1000).strftime('%Y-%m-%d %H:%M:%S')
            symbol = item['symbol'].replace('USDTM', '').replace('XBT', 'BTC') + 'USDT'
            status = "🔴 LONG PAY" if rate > 0.1 else "🟢 SHORT PAY" if rate < -0.1 else "🟡 NEUTRAL"
            rows.append([timestamp, date_str, 'KuCoin', symbol, round(rate, 4), next_time, status])
        
        if rows:
            self.worksheet.append_rows(rows)
            print(f"✅ {len(rows)} lignes ajoutées")
    
    def run(self):
        print("🚀 Collecte des funding rates...")
        binance_data = self.get_binance_funding()
        kucoin_data = self.get_kucoin_funding()
        self.save_data(binance_data, kucoin_data)
        print("✅ Collecte terminée!")

if __name__ == "__main__":
    collector = FundingRateCollector()
    collector.run()
