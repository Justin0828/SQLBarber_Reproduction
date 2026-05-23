from configparser import ConfigParser


def create_db_controller(target_dbms, config_path):
    config = ConfigParser()
    config.read(config_path)
    
    if target_dbms == "postgres":
        from db_controller.postgresql_controller import PostgreSQLController
        return PostgreSQLController.from_file(config)
    elif target_dbms == "mysql":
        from db_controller.mysql_controller import MySQLController
        return MySQLController.from_file(config)
    else:
        raise NotImplementedError("This DBMS product is not supported yet! Only PostgreSQL and MySQL is supported now!")
