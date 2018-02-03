#!/bin/bash

# Expects a lib directory in course home.
mkdir -p /home/${NB_USER}/.ipython
chown ${NB_USER}:${NB_GID} /home/${NB_USER}/.ipython
if [ ! -L "/home/$NB_USER/.ipython/lib" ]; then 
  ln -s /srv/nbgrader/${COURSE_NAME}/supporting_material/lib /home/$NB_USER/.ipython/lib
fi

chown -h ${ADMIN_INSTRUCTOR_UID}:${INSTRUCTOR_GID} /home/$NB_USER/.ipython/lib

# Expects a bin directory.
export PATH=/srv/nbgrader/${COURSE_NAME}/supporting_material/bin:$PATH

# To have prolog syntax highlight in output cells.
CODE_MIRROR_DIR=/opt/conda/lib/python3.6/site-packages/notebook/static/components/codemirror/mode
if [ ! -d "${CODE_MIRROR_DIR}/prolog" ]; then
  cp -r /srv/nbgrader/${COURSE_NAME}/supporting_material/prolog_codemirror/prolog ${CODE_MIRROR_DIR}
fi

# Symlink to data folder
if [ ! -L "/home/$NB_USER/data_readonly" ]; then 
  ln -s /srv/nbgrader/${COURSE_NAME}/supporting_material/data /home/$NB_USER/data_readonly
fi
chown -h ${ADMIN_INSTRUCTOR_UID}:${INSTRUCTOR_GID} /home/$NB_USER/data_readonly

# Install sql magic.
cd /srv/nbgrader/${COURSE_NAME}/supporting_material/lib/ipython-sql
/opt/conda/bin/python setup.py install
cd ${OLDPWD}

# To have prolog syntax highlight in input cells.
mkdir -p /home/${NB_USER}/.jupyter/custom
chown ${ADMIN_INSTRUCTOR_UID}:${INSTRUCTOR_GID} /home/${NB_USER}/.jupyter/custom 
cp  /srv/nbgrader/${COURSE_NAME}/supporting_material/jupyter_custom_js/custom.js /home/${NB_USER}/.jupyter/custom
chown ${ADMIN_INSTRUCTOR_UID}:${INSTRUCTOR_GID} /home/${NB_USER}/.jupyter/custom/custom.js
 
