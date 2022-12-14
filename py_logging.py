import logging
import sys
from logging.handlers import RotatingFileHandler

from py_config import ConfigFactory


class LoggerFactory(logging.Logger):
    def __init__(self, config_factory: ConfigFactory):
        super(LoggerFactory, self).__init__('py_flask')
        self.cfg = config_factory

    def get_logger(self) -> logging.Logger:
        # 日志显示格式
        formatter = logging.Formatter(
            fmt="%(asctime)s.%(msecs)03d [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s", datefmt="%Y-%b-%d %H:%M:%S")
        # 滚动日志文件
        file_handler_dict = dict(self.cfg.items('logger'))
        file_handler_dict['maxBytes'] = int(file_handler_dict['maxBytes'])
        file_handler_dict['backupCount'] = int(
            file_handler_dict['backupCount'])
        file_handler = RotatingFileHandler(**file_handler_dict)
        file_handler.setFormatter(formatter)
        # 控制台日志
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        # 添加日志处理
        __logger = logging.getLogger()
        __logger.addHandler(file_handler)
        __logger.addHandler(stream_handler)
        # 设置默认日志等级
        __logger.setLevel(self.cfg.getint('default', 'logger_level'))
        return __logger

