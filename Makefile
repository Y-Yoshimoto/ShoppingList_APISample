# Makefile for shoppinglist_apisample
rebuild:
	docker-compose down
	docker-compose up -d --build

restart:
	docker-compose down
	docker-compose up -d

appRestart:
	docker-compose restart unitpy_api
	# docker-compose up -d --build sendmail_api

reload:
	docker-compose up -d --build

RegName=webappstestyyreg.azurecr.io
push:
	docker-compose build
	docker tag nginx_forunit webappstestyyreg.azurecr.io/nginx_forunit
	docker push webappstestyyreg.azurecr.io/nginx_forunit
	docker tag nginx_forunit webappstestyyreg.azurecr.io/unitpy_api
	docker push webappstestyyreg.azurecr.io/unitpy_api
	docker tag nginx_forunit webappstestyyreg.azurecr.io/unit_mariadb
	docker push webappstestyyreg.azurecr.io/unit_mariadb
	docker tag nginx_forunit webappstestyyreg.azurecr.io/express_api
	docker push webappstestyyreg.azurecr.io/express_api
	docker tag nginx_forunit webappstestyyreg.azurecr.io/postfix_custom
	docker push webappstestyyreg.azurecr.io/postfix_custom