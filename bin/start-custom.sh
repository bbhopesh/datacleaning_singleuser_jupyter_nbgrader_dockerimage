#!/bin/bash

# User should be set to root in the docker file before calling this.

set -e

if [[ "$NB_USER" == "jovyan" ]]; then
	echo "We need to have hub usernames for nbgrader to work instead of static user jovyan."
	exit 1
fi

userdel -rf jovyan

############################ Create user instructor group ################################
if id "${NB_USER}" >/dev/null 2>&1; then
	echo "User ${NB_USER} exists."
else
	echo "User does not exist. Adding user ${NB_USER} (${NB_UID})"
	useradd -u ${NB_UID} ${NB_USER}
	# User home directory will already exist because SystemUserSpawner takes care of that.
fi

if getent group ${INSTRUCTOR_GROUP} > /dev/null 2>&1; then
        echo "Group ${INSTRUCTOR_GROUP} exists."
else
	echo "Group does not exist. Adding group ${INSTRUCTOR_GROUP} (${INSTRUCTOR_GID})"
	groupadd -g ${INSTRUCTOR_GID} ${INSTRUCTOR_GROUP}
fi

# Change group id of the group. Following line is a no op if there is no change.
groupmod -g ${INSTRUCTOR_GID} ${INSTRUCTOR_GROUP}

if [[ "${IS_INSTRUCTOR}" == "true" ]] ; then
	usermod -u ${NB_UID} -g ${INSTRUCTOR_GID} ${NB_USER}
else
	usermod -u ${NB_UID} -g ${NB_GID} ${NB_USER}
fi
###################################################################################

cd /home/${NB_USER}

########################## Set up directories #####################################
mkdir -p /home/${NB_USER}/.jupyter
chown ${NB_USER} /home/${NB_USER}/.jupyter

chown ${ADMIN_INSTRUCTOR_UID}:${INSTRUCTOR_GID} /srv/nbgrader/${COURSE_NAME}

# Make exchange directory readable and writable by everyone.
# Take exchange directory as environment variable later.
# This should be same volume mounted on each user's docker container.
chmod 777 /srv/nbgrader/exchange
chown ${ADMIN_INSTRUCTOR_UID}:${INSTRUCTOR_GID} /srv/nbgrader/exchange

if [[ "${IS_INSTRUCTOR}" == "true" && ! -L "/home/$NB_USER/${COURSE_NAME}" ]] ; then
  # If the user is instructor then point to course directory from user's home.
  ln -sf /srv/nbgrader/${COURSE_NAME} /home/$NB_USER/${COURSE_NAME} 
fi

# chown -hR ${NB_USER}:${NB_GROUP} /home/${NB_USER}
##################################################################################


################## Disable extensions for students #############################
if [[ "${IS_INSTRUCTOR}" != "true" ]] ; then
  jupyter nbextension disable --sys-prefix create_assignment/main
  jupyter nbextension disable --sys-prefix formgrader/main --section=tree
  jupyter serverextension disable --sys-prefix nbgrader.server_extensions.formgrader
fi
################################################################################

source datacleaning-setup.sh

# Start the single user notebook.
exec /usr/local/bin/start-singleuser-custom.sh $*

