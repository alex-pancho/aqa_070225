import logging

# Налаштування конфігурації логування
logging.basicConfig(
    filename="example.log",
    encoding="utf8",
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
)

logging.debug('Це повідомлення рівня DEBUG') # 10
logging.info('Це повідомлення рівня INFO') # 20
logging.warning('Це повідомлення рівня WARNING') # 30
logging.error('Це повідомлення рівня ERROR')  # 40
logging.critical('Це повідомлення рівня CRITICAL')  # 50
logging.debug('Це повідомлення рівня DEBUG') # 10