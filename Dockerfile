ARG DOCKER_NOTEBOOK_IMAGE
FROM $DOCKER_NOTEBOOK_IMAGE

ARG JUPYTERHUB_VERSION
RUN python3 -m pip install --no-cache jupyterhub==$JUPYTERHUB_VERSION
RUN /opt/conda/bin/conda install -c conda-forge nbgrader
RUN /opt/conda/bin/conda install psycopg2
RUN /opt/conda/bin/conda install prettytable
RUN /opt/conda/bin/conda install sqlalchemy
RUN /opt/conda/bin/conda install sqlparse
RUN /opt/conda/bin/conda install six
RUN /opt/conda/bin/conda install pgspecial
#RUN /opt/conda/bin/conda install ipython-genutils

USER root

COPY ./bin/start-custom.sh /usr/local/bin
COPY ./bin/start-singleuser-custom.sh /usr/local/bin
COPY ./bin/datacleaning-setup.sh /usr/local/bin
COPY ./nbgrader_config.py /etc/jupyter
# This line is necessary because in the start script we delete user jovyan and without this line wordir is /home/jovyan
WORKDIR /root
