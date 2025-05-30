print("🚀 Test du bot funding rates")
print("✅ Le script Python fonctionne!")

# Test basique
import requests
print("✅ Requests importé")

try:
    response = requests.get("https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT")
    data = response.json()
    print(f"✅ Test Binance OK: BTC funding = {data['lastFundingRate']}")
except Exception as e:
    print(f"❌ Erreur: {e}")

print("🎯 Test terminé!")
