CURRENT_DIR=$(shell pwd)

APP=$(shell basename ${CURRENT_DIR})

APP_CMD_DIR=${CURRENT_DIR}/cmd

REGISTRY=${REGISTRY}
PROJECT_NAME=${PROJECT_NAME}

TAG=latest
ENV_TAG=latest

# Including
include .env

run:
	docker-compose -f docker-compose.yml up --force-recreate

dc-config:
	docker-compose -f docker-compose.yml config

clear:
	rm -rf ${CURRENT_DIR}/bin/*

migrate-up:
	python3 manage.py migrate

mark-as-production-image:
	docker tag ${REGISTRY}/${IMG_NAME}:${TAG} ${REGISTRY}/${IMG_NAME}:production
	docker push ${REGISTRY}/${IMG_NAME}:production

build-image:
	docker build --rm -t ${REGISTRY}/${PROJECT_NAME}/${APP}:${TAG} .
	docker tag ${REGISTRY}/${PROJECT_NAME}/${APP}:${TAG} ${REGISTRY}/${PROJECT_NAME}/${APP}:${ENV_TAG}

push-image:
	docker push ${REGISTRY}/${PROJECT_NAME}/${APP}:${TAG}
	docker push ${REGISTRY}/${PROJECT_NAME}/${APP}:${ENV_TAG}

install-packages:
	pip3 install -r requirements.txt

messages-uz:
	django-admin makemessages -l uz --ignore venv

messages-ru:
	django-admin makemessages -l ru --ignore venv

compile-language:
	django-admin compilemessages --ignore venv
	

