class Config(object):
    """
    Common configurations
    """
    DEBUG = True

# Put any configurations here that are common across all environments.

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(DevelopmentConfig):
    """
    Testing configuration
    """

    TESTING = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
