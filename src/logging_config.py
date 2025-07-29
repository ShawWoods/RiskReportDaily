import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logging(log_file='logs/risk_report.log'):
    logger = logging.getLogger('RiskReport')
    logger.setLevel(logging.INFO)
    
    # 文件日志，按天分割
    file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=30)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'))
    logger.addHandler(file_handler)
    
    # 控制台日志
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(console_handler)
    
    return logger
