import os
import sys
import time
from functools import wraps
from pathlib import Path
import loguru
from tools.paths import project_path as paths


# 单例类的装饰器
def singleton_class_decorator(cls):
    _instance = {}
    @wraps(cls)
    def wrapper_class(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return wrapper_class

def log_path():
    _path = str(Path(sys.argv[0]).parent)
    _path = _path.replace("\\", "/")
    _path += '/logs.log'
    return _path


@singleton_class_decorator
class Logger:
    def __init__(self):
        self.clear_log_file()
        self.logger_add()

    @staticmethod
    def clear_log_file():
        log_file_path = paths() + "./logs.log"
        log_dir = os.path.dirname(log_file_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        with open(log_file_path, 'w', encoding='utf-8') as log_file:
            log_file.truncate(0)

    @staticmethod
    def logger_add():
        loguru.logger.add(
            sink= log_path(),
            level="ERROR",
            rotation='00:00',
            retention='1 day',
            compression='zip',
            encoding="utf-8",
            enqueue=True
        )

    @property
    def get_logger(self):
        return loguru.logger

logger = Logger().get_logger


if __name__ == '__main__':
    # logger.info("测试日志")
    print(log_path())