from ric.settings import use_mysql_app


class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in use_mysql_app:
            return 'mysql'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in use_mysql_app:
            return 'mysql'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in use_mysql_app:
            return db == 'mysql'
        return db == 'default'
