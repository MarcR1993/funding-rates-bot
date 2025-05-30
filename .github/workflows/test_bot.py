#!/usr/bin/env python3
print("✅ Bot de test démarré")

import sys
print(f"✅ Python version: {sys.version}")

try:
    import requests
    print("✅ Requests importé avec succès")
    
    # Test simple Binance
    response = requests.get("https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT", timeout=10)
    if response.status_code == 200:
        data = response.json()
        funding_rate = float(data['lastFundingRate']) * 100
        print(f"✅ Test Binance réussi - BTC funding rate: {funding_rate:.4f}%")
    else:
        print(f"❌ Erreur Binance: {response.status_code}")
        
except Exception as e:
    print(f"❌ Erreur: {e}")

print("🎯 Test terminé avec succès!")
