# Makefile for shoppinglist_apisample
rebuild:
	docker-compose down
	docker-compose up -d --build

restart:
	docker-compose down
	docker-compose up -d

reload:
	docker-compose restart unitpy_api