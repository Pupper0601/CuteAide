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
        self.logger_add()

    def get_project_path(self, project_path=None):
        if project_path is None:
            # 当前项目文件的，绝对真实路径
            # 路径，一个点代表当前目录，两个点代表当前目录的上级目录
            project_path = paths()
        # 返回当前项目路径
        return project_path

    def get_log_path(self):
        # 项目目录
        project_path = self.get_project_path()
        # 项目日志目录
        creat_time = time.strftime("%Y-%m-%d", time.localtime())
        logs_file_path = Path(project_path).joinpath('logs', creat_time)
        if logs_file_path.exists():
            logs_path = logs_file_path
        else:
            try:
                logs_file_path.mkdir(parents=True)
            except Exception as e:
                print(f"创建文件报错: {e}")
            logs_path = logs_file_path
        # 日志文件名
        project_log_filename = '{}.log'.format(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()) )
        # 日志文件路径
        project_log_path = Path(logs_path).joinpath(logs_path, project_log_filename)
        # 返回日志路径
        return project_log_path

    def logger_add(self):
        loguru.logger.add(
            # 水槽，分流器，可以用来输入路径
            sink=self.get_log_path(),
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