import os
from enum import Enum
from functools import lru_cache
from typing import Literal, Optional, Self

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Env(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    STAGE = "stage"
    PROD = "prod"
    TEST = "test"


class Config(BaseSettings):
    model_config = ConfigDict(extra='allow')

    app_host: str
    app_port: int
    log_level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    log_dir: str

    @staticmethod
    @lru_cache
    def from_env() -> Self:
        return Config(
            _env_file=f'.env.{os.getenv("ENV", Env.LOCAL.value)}',
            _env_file_encoding="utf-8"
        )

    def logging_config(self):
        return {
            'version': 1,
            'formatters': {
                'simple': {'format': '[%(name)s] %(message)s'},
                'complex': {
                    'format': '%(asctime)s|%(levelname)s|%(name)s|%(filename)s:%(lineno)d|%(message)s'
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'complex',
                    'level': 'DEBUG',
                },
                'rolling_file': {
                    'level': 'DEBUG',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': self.log_dir + '/app.log',
                    'maxBytes': 1024 * 1024 * 5,  # 5 MB
                    'backupCount': 5,
                    'formatter': 'complex',
                },
                'file': {
                    'class': 'logging.FileHandler',
                    'filename': 'error.log',
                    'formatter': 'complex',
                    'level': 'ERROR',
                },
            },
            'loggers': {
                'app': {
                    'handlers': ['console', 'rolling_file'],
                    'level': self.log_level,
                }
            },
        }
