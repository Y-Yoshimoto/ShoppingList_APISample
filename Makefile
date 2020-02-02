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