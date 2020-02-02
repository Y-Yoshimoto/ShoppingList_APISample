FROM mariadb
LABEL  maintainer "y.yoshimoto"

# 設定ファイルのコピー
COPY my.cnf /etc/mysql/my.cnf
RUN mkdir -p /usr/local/etc/my.cnf.d
# ポートエクスポート
EXPOSE 3306

# 初期構築データのコピー
COPY unit_startup.sql /docker-entrypoint-initdb.d/unit_startup.sql
