include .env

.DEFAULT_GOAL=notebook_image

pull:
	docker pull $(DOCKER_NOTEBOOK_IMAGE)

notebook_image: pull Dockerfile
	docker build -t $(LOCAL_NOTEBOOK_IMAGE) \
		--build-arg JUPYTERHUB_VERSION=$(JUPYTERHUB_VERSION) \
		--build-arg DOCKER_NOTEBOOK_IMAGE=$(DOCKER_NOTEBOOK_IMAGE) .

