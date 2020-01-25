-- mysql -P 33306 -u shoppinglistUser -h 127.0.0.1 -p shoppinglist
SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTION = utf8;
create database shoppinglist;
-- create user itmsUser@'%' identified by 'Password';
GRANT all on shoppinglist.* TO `shoppinglistUser`@'%' IDENTIFIED BY 'Password';
GRANT all on shoppinglist.* TO `shoppinglistUser`@'localhost' IDENTIFIED BY 'Password';
-- SELECT user,host FROM mysql.user;
-- grant all on itms.* to itmsUser;
use shoppinglist;

-- data
CREATE TABLE t_shoppinglist (
    id int PRIMARY KEY AUTO_INCREMENT,  -- プライマーキー
    productName VARCHAR(64) NOT NULL, -- 商品名
    price int NOT NULL, -- 価格
    flag int NOT NULL -- 削除フラッグ(0:有効,1:削除+パスワード空白)
);
INSERT INTO t_shoppinglist VALUES (1,'スイカ',100,0);
INSERT INTO t_shoppinglist VALUES (2,'トマト',120,0);
INSERT INTO t_shoppinglist VALUES (3,'きゅうり',300,0);
-- SELECT * FROM t_shoppinglist;
