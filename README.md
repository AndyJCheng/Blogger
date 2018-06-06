# Blogger
## install mysql-8.0.11-winx64  
   1 download mysql8.0 zip and unzip.  
   2 create my.int and data folder under mysql.  
     my.ini:  
     [mysqld]  
     # 设置3306端口  
     port=3306  
     # 设置mysql的安装目录  
     basedir=D:\mysql-8.0.11-winx64  
     # 设置mysql数据库的数据的存放目录  
     datadir=D:\mysql-8.0.11-winx64\data  
     # 允许最大连接数  
     max_connections=200  
     # 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统  
     max_connect_errors=10  
     # 服务端使用的字符集默认为UTF8  
     character-set-server=utf8  
     # 创建新表时将使用的默认存储引擎  
     default-storage-engine=INNODB  
     [mysql]  
     # 设置mysql客户端默认字符集  
     default-character-set=utf8  
     [client]  
     # 设置mysql客户端连接服务端时默认使用的端口  
     port=3306  
     default-character-set=utf8  
   3 mysql --initialize --console,record temporary password.  
      mysql --install  
      net start mysql  
      ALTER USER "root"@"localhost" IDENTIFIED  BY "你的新密码";  
   4  change root password authorization way.  
      ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '5032';  

