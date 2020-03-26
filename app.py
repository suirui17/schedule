import os

from todoism import create_app

import pymysql
pymysql.install_as_MySQLdb()

config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)


if __name__ == '__main__':
    app.run(debug=True)
