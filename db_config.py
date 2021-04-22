from app import app
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

# Rows from cursors will always be of type dict || cursorclass=DictCursor
mysql = MySQL(cursorclass=DictCursor)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "tux"
app.config['MYSQL_DATABASE_PASSWORD'] = "licet@123"
app.config['MYSQL_DATABASE_DB'] = "miles"
app.config['MYSQL_DATABASE_HOST'] = "vpn.opencloud.pattarai.in"
mysql.init_app(app)
