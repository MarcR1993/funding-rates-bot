"""
Configuration du Bot de Funding Rate Arbitrage
==============================================

Ce fichier contient toutes les configurations du bot.
Modifie ces valeurs selon tes besoins sans toucher au code principal.
"""

import os
from typing import List, Dict

class Config:
    """Configuration principale du bot"""
    
    # ==================== CRYPTOS À SURVEILLER ====================
    SYMBOLS: List[str] = [
        'BTC',    # Bitcoin
        'ETH',    # Ethereum  
        'SOL',    # Solana
        'ADA',    # Cardano
        'MATIC',  # Polygon
        'DOT',    # Polkadot
        'AVAX'    # Avalanche
    ]
    
    # ==================== SEUILS DE TRADING ====================
    # Profit minimum pour considérer une opportunité (en %)
    MIN_PROFIT_THRESHOLD: float = 0.005  # 0.5% pour 8h
    
    # Taille de position par défaut (en USD)
    POSITION_SIZE: int = 1000
    
    # Écart minimum de funding rate pour analyser (en %)
    MIN_RATE_DIFFERENCE: float = 0.0001  # 0.01%
    
    # ==================== TIMING ====================
    # Intervalle entre les scans (en minutes)
    SCAN_INTERVAL: int = 30
    
    # Timeout pour les requêtes API (en secondes)  
    REQUEST_TIMEOUT: int = 10
    
    # Délai minimum entre requêtes vers le même exchange (en secondes)
    RATE_LIMIT_DELAY: float = 0.5
    
    # ==================== EXCHANGES ====================
    # Exchanges à utiliser (retire ceux que tu ne veux pas)
    ENABLED_EXCHANGES: List[str] = [
        'binance',
        'bybit', 
        'okx',
        'bitget',
        'kucoin'
    ]
    
    # Frais estimés par exchange (maker + taker + withdrawal en %)
    EXCHANGE_FEES: Dict[str, float] = {
        'Binance': 0.08,   # Très liquide, frais compétitifs
        'Bybit': 0.08,     # Interface user-friendly
        'OKX': 0.09,       # Bon pour les gros volumes
        'Bitget': 0.10,    # Copy trading disponible
        'KuCoin': 0.09     # Large sélection d'altcoins
    }
    
    # ==================== ESTIMATION DU SLIPPAGE ====================
    # Slippage estimé par crypto (en %)
    SLIPPAGE_ESTIMATES: Dict[str, float] = {
        'BTC': 0.01,     # Très liquide
        'ETH': 0.02,     # Très liquide
        'SOL': 0.03,     # Bonne liquidité
        'ADA': 0.04,     # Liquidité moyenne
        'MATIC': 0.04,   # Liquidité moyenne
        'DOT': 0.03,     # Bonne liquidité
        'AVAX': 0.03     # Bonne liquidité
    }
    
    # ==================== LOGS ET FICHIERS ====================
    # Niveau de log (DEBUG, INFO, WARNING, ERROR)
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    
    # Fichier de log
    LOG_FILE: str = 'funding_rate_bot.log'
    
    # Dossier pour sauvegarder les opportunités
    DATA_DIR: str = 'data'
    
    # Garder les logs pendant X jours
    LOG_RETENTION_DAYS: int = 30
    
    # ==================== NOTIFICATIONS (Future) ====================
    # Activer les notifications (pas encore implémenté)
    ENABLE_NOTIFICATIONS: bool = False
    
    # Seuil pour envoyer une notification (en %)
    NOTIFICATION_THRESHOLD: float = 0.01  # 1% ou plus
    
    # ==================== MODE DÉVELOPPEMENT ====================
    # Mode debug (plus de logs, pas de rate limiting strict)
    DEBUG_MODE: bool = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # Simuler les requêtes (pour tester sans appeler les APIs)
    SIMULATE_REQUESTS: bool = False
    
    # ==================== PARAMÈTRES AVANCÉS ====================
    # Nombre maximum de tentatives en cas d'erreur API
    MAX_RETRIES: int = 3
    
    # Délai entre les tentatives (en secondes)
    RETRY_DELAY: float = 2.0
    
    # Nombre maximum d'opportunités à afficher
    MAX_OPPORTUNITIES_DISPLAY: int = 5
    
    # Sauvegarder toutes les opportunités (même non rentables)
    SAVE_ALL_OPPORTUNITIES: bool = True

class DevelopmentConfig(Config):
    """Configuration pour le développement"""
    DEBUG_MODE = True
    LOG_LEVEL = 'DEBUG'
    SCAN_INTERVAL = 10  # Scan plus fréquent en dev
    MIN_PROFIT_THRESHOLD = 0.001  # Seuil plus bas pour tester

class ProductionConfig(Config):
    """Configuration pour la production"""
    DEBUG_MODE = False
    LOG_LEVEL = 'INFO'
    SCAN_INTERVAL = 30
    MIN_PROFIT_THRESHOLD = 0.005

# ==================== SÉLECTION DE LA CONFIG ====================
# Change ceci selon ton environnement
ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')

if ENVIRONMENT == 'development':
    config = DevelopmentConfig()
elif ENVIRONMENT == 'production':
    config = ProductionConfig()
else:
    config = Config()

# ==================== EXEMPLE DE CONFIGURATION PERSONNALISÉE ====================
"""
Pour personnaliser ton bot, crée un fichier config_local.py avec :

from config import Config

class MyConfig(Config):
    # Surveillance seulement BTC et ETH
    SYMBOLS = ['BTC', 'ETH']
    
    # Position plus importante
    POSITION_SIZE = 5000
    
    # Seuil plus élevé
    MIN_PROFIT_THRESHOLD = 0.01  # 1%
    
    # Seulement 3 exchanges
    ENABLED_EXCHANGES = ['binance', 'bybit', 'okx']

config = MyConfig()
"""

# ==================== VALIDATION DE LA CONFIG ====================
def validate_config():
    """Valide la configuration"""
    errors = []
    
    if not config.SYMBOLS:
        errors.append("SYMBOLS ne peut pas être vide")
    
    if config.MIN_PROFIT_THRESHOLD <= 0:
        errors.append("MIN_PROFIT_THRESHOLD doit être positif")
    
    if config.POSITION_SIZE <= 0:
        errors.append("POSITION_SIZE doit être positif")
    
    if not config.ENABLED_EXCHANGES:
        errors.append("ENABLED_EXCHANGES ne peut pas être vide")
    
    if errors:
        raise ValueError(f"Configuration invalide: {', '.join(errors)}")
    
    return True

# Valide automatiquement au chargement
if __name__ != "__main__":
    validate_config()
