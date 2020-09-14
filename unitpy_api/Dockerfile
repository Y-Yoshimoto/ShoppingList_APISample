FROM nginx/unit:1.19.0-python3.7
# https://github.com/nginx/unit/tree/master/pkg/docker
LABEL  maintainer "y.yoshimoto"

# Install pip
RUN apt-get -y update\
    && apt-get install -y python3-pip mariadb-client libmariadbclient-dev\
    && apt-get clean
#pip freeze > requirements.lock
COPY requirements.txt /docker-entrypoint.d/requirements.txt
RUN pip3 install -r /docker-entrypoint.d/requirements.txt && pip3 freeze > requirements.lock

# アプリケーションを配置
RUN mkdir -p /www/ShoppingList
COPY contents/*.py /www/ShoppingList/

## コンフィグファイル設置
COPY appconfig.json /docker-entrypoint.d/
EXPOSE 8300
