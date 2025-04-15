# 创建日志处理器
import logging
from colorlog import ColoredFormatter

def setup_logging():
    """
    设置日志格式和处理器
    """

    # 创建一个 StreamHandler
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    # 配置彩色格式器
    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'bold_red',
        }
    )
    handler.setFormatter(formatter)

    # 应用到 root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers = []  # 清除其他 handler，避免重复打印
    logger.addHandler(handler)