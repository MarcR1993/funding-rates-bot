# 🚀 Funding Rates Bot

> **Bot d'arbitrage crypto professionnel** - Surveillance des funding rates en temps réel sur multiple exchanges

[![Live Demo](https://img.shields.io/badge/🔴_LIVE_DEMO-GitHub_Pages-success?style=for-the-badge)](https://marcr1993.github.io/funding-rates-bot/)
[![API Status](https://img.shields.io/badge/API-Binance_Live-orange?style=for-the-badge)](https://fapi.binance.com/fapi/v1/premiumIndex)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

## 📊 Aperçu

Interface **No-Code** pour surveiller et analyser les **funding rates** des cryptomonnaies en temps réel. Identifie automatiquement les **opportunités d'arbitrage** avec calculs APR précis.

### 🎯 Fonctionnalités Principales

- **📈 Dashboard Live** - Vue d'ensemble multi-exchanges avec données Binance temps réel
- **⚡ Arbitrage Intelligent** - TOP 5 opportunités avec calculs APR automatiques
- **🔧 Configuration Flexible** - Gestion personnalisable des cryptos et exchanges
- **⏰ Timing Précis** - Synchronisation des horaires de funding entre exchanges
- **📱 Interface Moderne** - Design responsive avec glassmorphism

## 🖥️ Demo en Direct

**🔗 [Accéder au Bot Live](https://marcr1993.github.io/funding-rates-bot/)**

![Dashboard Preview](https://via.placeholder.com/800x400/667eea/ffffff?text=Funding+Rates+Bot+Dashboard)

## 🚀 Démarrage Rapide

### Option 1: Utilisation Directe
```
👆 Clique sur le lien "Live Demo" ci-dessus
✅ Aucune installation requise
🔴 Données Binance en temps réel
```

### Option 2: Hébergement Local
```bash
# Clone le repository
git clone https://github.com/MarcR1993/funding-rates-bot.git
cd funding-rates-bot

# Ouvre index.html dans un navigateur
# Ou démarre un serveur local :
python -m http.server 8000
# Puis ouvre http://localhost:8000
```

## 📋 Guide d'Utilisation

### 🎛️ **Dashboard**
- **Statut Bot** : Indicateur temps réel de connexion API
- **Vue d'ensemble** : Comparaison funding rates sur 4 exchanges
- **Statistiques** : Cryptos surveillées, exchanges connectés, pairs actives

### ⚡ **Arbitrage**
- **Horaires Funding** : Synchronisation précise des 4 exchanges
- **TOP 5 Opportunités** : Meilleures stratégies avec APR calculé
- **Calculs Détaillés** : Net funding, spread, settlement timing

### 🔧 **Configuration**
- **Cryptos** : Sélection personnalisable (BTC, ETH, SOL, etc.)
- **Exchanges** : Activation/désactivation des plateformes
- **Paramètres** : Fréquence collecte, seuils d'alerte

## 🏗️ Architecture Technique

### 📡 **APIs Intégrées**
- **Binance Futures** : Données temps réel (connecté)
- **KuCoin, Bybit, OKX** : En cours d'intégration

### 🧮 **Calculs Financiers**
```javascript
// Formule APR
APR = (Net Funding Rate × 365 × 3) × 100

// Formule Spread  
Spread = (|Rate Max - Rate Min| / Moyenne) × 100

// Net Funding
Net = Rate Exchange Short - Rate Exchange Long
```

### ⏰ **Horaires de Funding**
- **Binance/KuCoin/Bybit** : 00:00, 08:00, 16:00 UTC (synchronisés)
- **OKX** : 01:00, 09:00, 17:00 UTC (décalage +1h)

## 🎨 Interface

### 🌟 **Design Moderne**
- **Glassmorphism** avec effets backdrop-filter
- **Animations fluides** et micro-interactions
- **Responsive** - Compatible mobile/desktop
- **Dark theme** avec dégradés purple/blue

### 📊 **Visualisation**
- **Tableaux interactifs** avec tri et filtres
- **Badges colorés** par exchange (🟡 Binance, 🟢 KuCoin, etc.)
- **Indicateurs visuels** : APR, spread, synchronisation

## ⚙️ Configuration Avancée

### 🔒 **Sécurité**
- **Lecture seule** : Aucune clé API privée requise
- **Données publiques** : Utilise uniquement les endpoints publics
- **CORS-friendly** : Fonctionne sur GitHub Pages

### 🚀 **Performance**
- **Auto-refresh** : Mise à jour toutes les 30 secondes
- **Cache intelligent** : Évite les appels API redondants
- **Fallback** : Mode dégradé si API indisponible

## 🛠️ Développement

### 📁 **Structure du Projet**
```
funding-rates-bot/
├── index.html              # Application principale
├── README.md               # Documentation
├── config/
│   └── example.json       # Configuration exemple
└── docs/
    └── api-reference.md   # Référence API
```

### 🔧 **Technologies**
- **Frontend** : HTML5, CSS3, Vanilla JavaScript
- **APIs** : Binance Futures, REST endpoints
- **Styling** : CSS Grid, Flexbox, Custom Properties
- **Hosting** : GitHub Pages, Netlify compatible

### 🎯 **Roadmap**

#### 🔄 **V2.0 - Prochaines fonctionnalités**
- [ ] **Intégration complète** KuCoin + Bybit + OKX APIs
- [ ] **Historique** des funding rates avec graphiques
- [ ] **Alertes** push notifications pour opportunités
- [ ] **Export** Google Sheets automatique

#### 🤖 **V3.0 - Automatisation**
- [ ] **GitHub Actions** - Collecte automatisée toutes les 8h
- [ ] **Webhook** intégrations (Discord, Slack, Telegram)
- [ ] **Portfolio** tracking avec positions ouvertes
- [ ] **Backtesting** historique des stratégies

## 📈 Exemples d'Utilisation

### 🎯 **Stratégie Arbitrage Typique**
```
1. Bot détecte: BTC funding rate différence >0.05%
   • Binance: +0.08% (short BTC)
   • KuCoin: +0.03% (long BTC)

2. Calcul automatique:
   • Net funding: +0.05% par 8h
   • APR projeté: +54.75%
   • Settlement: Synchronisé (pas de décalage)

3. Action recommandée:
   • Short BTC/USDT sur Binance
   • Long BTC/USDT sur KuCoin
   • Profit garanti à chaque funding
```

### 📊 **Monitoring Continu**
- **Dashboard** : Surveillance 24/7 des 7 cryptos principales
- **Alertes** : Notification dès qu'une opportunité >50% APR apparaît
- **Timing** : Synchronisation parfaite avec horaires funding

## 🤝 Contribution

### 🐛 **Bugs & Suggestions**
Ouvre une [issue](https://github.com/MarcR1993/funding-rates-bot/issues) pour :
- Rapporter des bugs
- Proposer des améliorations
- Demander des nouvelles fonctionnalités

### 🔀 **Pull Requests**
1. Fork le projet
2. Crée ta feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit tes changes (`git commit -m 'Add: Amazing feature'`)
4. Push sur la branch (`git push origin feature/AmazingFeature`)
5. Ouvre une Pull Request

## 📄 License

Distribué sous licence **MIT**. Voir `LICENSE` pour plus d'informations.

## 📧 Contact

**Marc R** - [@MarcR1993](https://github.com/MarcR1993)

**Project Link**: [https://github.com/MarcR1993/funding-rates-bot](https://github.com/MarcR1993/funding-rates-bot)

---

### ⭐ **Si ce projet t'aide, donne-lui une étoile !**

![GitHub Stars](https://img.shields.io/github/stars/MarcR1993/funding-rates-bot?style=social)

---

## 🏷️ **Keywords**
`crypto` `arbitrage` `funding-rates` `binance` `trading-bot` `defi` `javascript` `no-code` `real-time` `dashboard`
