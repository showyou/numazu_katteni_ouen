沼津周辺のお店を勝手に応援するサイト

# 使い方

後でdocker-compose化するつもりですが、それまで待ってね
```sh
aptやyum等でmysql-serverかmariadb-serverとmysql-develかmariadb-develとgccとpython3-develをインストールして動かす
$ sudo systemctl start mariadb(かmysql)
$ mysql -u root 
パスワード変更(ROOTPASSWD, DBNAME, THISHOSTIP, YOURPASSWDは各自変更すること)
> UPDATE mysql.user SET password=password('ROOTPASSWD') WHERE user = 'root';
> CREATE DATABASE DBNAME;
> GRANT ALL PRIVILEGES ON DBNAME.* TO 'USERNAME'@'THISHOSTIP' IDENTIFIED BY 'YOURPASSWD';
> FLUSH PRIVILEGES;
> exit
$ git clone https://github.com/showyou/numazu_katteni_ouen.git
$ cd numazu_katteni_ouen
$ pipenv install
$ pipenv shell
$ cd numazu_shop
$ cp numazu_shop/settings.template.py numazu_shop/settings.py
$ vim numazu_shop/settings.py
SECRET_KEYを適当なものに変更
本番で動かす場合DEBUGはFalse, ALLOWED_HOSTS = ['0.0.0.0']にする
DBの部分は次のような感じにする(DBNAME, USERNAME, YOURPASSWD, HOSTNAME, PORTNUMBERは各自の環境に変えて下さい)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DBNAME',
        'USER': 'YOURUSERNAME',
        'PASSWORD': 'YOURPASSWD',
        'HOST': 'HOSTNAME',
        'PORT': 'PORTNUMBER',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
$ python3 manage.py migrate
$ python3 manage.py runserver
このホストの8000番にブラウザで繋げば表示されるはず
```
