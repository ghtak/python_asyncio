import logging
import logging.config
import logging.handlers
import os

from app.config import Config


class AppContext:
    config: Config = Config.from_env()
    logger = logging.getLogger('app')

    @classmethod
    def init_logging(cls):
        os.makedirs(cls.config.log_dir, exist_ok=True)
        logging.config.dictConfig(cls.config.logging_config())
