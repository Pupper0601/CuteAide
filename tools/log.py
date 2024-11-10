import time
from functools import wraps
from pathlib import Path
import loguru
from tools.paths import project_path as paths


# 单例类的装饰器
def singleton_class_decorator(cls):
    """
    装饰器，单例类的装饰器
    """
    # 在装饰器里定义一个字典，用来存放类的实例。
    _instance = {}

    # 装饰器，被装饰的类
    @wraps(cls)
    def wrapper_class(*args, **kwargs):
        # 判断，类实例不在类实例的字典里，就重新创建类实例
        if cls not in _instance:
            # 将新创建的类实例，存入到实例字典中
            _instance[cls] = cls(*args, **kwargs)
        # 如果实例字典中，存在类实例，直接取出返回类实例
        return _instance[cls]

    # 返回，装饰器中，被装饰的类函数
    return wrapper_class


@singleton_class_decorator
class Logger:
    def __init__(self):
        self.clear_log_file()
        self.logger_add()

    @staticmethod
    def clear_log_file():
        log_file_path = paths() + "./logs.log"
        with open(log_file_path, 'w', encoding='utf-8') as log_file:
            log_file.truncate(0)

    @staticmethod
    def logger_add():
        loguru.logger.add(
            # 水槽，分流器，可以用来输入路径
            sink= paths() + "./logs.log",
            # 日志创建周期
            rotation='00:00',
            # 保存
            retention='1 day',
            # 文件的压缩格式
            compression='zip',
            # 编码格式
            encoding="utf-8",
            # 具有使日志记录调用非阻塞的优点
            enqueue=True
        )

    @property
    def get_logger(self):
        return loguru.logger

logger =  Logger().get_logger


if __name__ == '__main__':
    logger.info("测试日志")