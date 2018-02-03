# Configuration file for jupyterhub.

import os
c = get_config()

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#c.Application.log_level = 30

#------------------------------------------------------------------------------
# JupyterHub(Application) configuration
#------------------------------------------------------------------------------

## An Application for starting a Multi-User Jupyter Notebook server.

## Maximum number of concurrent servers that can be active at a time.
#  
#  Setting this can limit the total resources your users can consume.
#  
#  An active server is any server that's not fully stopped. It is considered
#  active from the time it has been requested until the time that it has
#  completely stopped.
#  
#  If this many user servers are active, users will not be able to launch new
#  servers until a server is shutdown. Spawn requests will be rejected with a 429
#  error asking them to try again.
#  
#  If set to 0, no limit is enforced.
#c.JupyterHub.active_server_limit = 0

## Grant admin users permission to access single-user servers.
#  
#  Users should be properly informed if this is enabled.
#c.JupyterHub.admin_access = False

## DEPRECATED since version 0.7.2, use Authenticator.admin_users instead.
#c.JupyterHub.admin_users = set()

## Allow named single-user servers per user
#c.JupyterHub.allow_named_servers = False

## Answer yes to any questions (e.g. confirm overwrite)
#c.JupyterHub.answer_yes = False

## PENDING DEPRECATION: consider using service_tokens
#  
#  Dict of token:username to be loaded into the database.
#  
#  Allows ahead-of-time generation of API tokens for use by externally managed
#  services, which authenticate as JupyterHub users.
#  
#  Consider using service_tokens for general services that talk to the JupyterHub
#  API.
#c.JupyterHub.api_tokens = {}

## Class for authenticating users.
#  
#  This should be a class with the following form:
#  
#  - constructor takes one kwarg: `config`, the IPython config object.
#  
#  - is a tornado.gen.coroutine
#  - returns username on success, None on failure
#  - takes two arguments: (handler, data),
#    where `handler` is the calling web.RequestHandler,
#    and `data` is the POST form data from the login page.
#c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
#c.JupyterHub.authenticator_class = 'jhub_remote_user_authenticator.remote_user_auth.RemoteUserAuthenticator'
c.JupyterHub.authenticator_class = 'ischool_shibboleth_logout.remote_user_auth.RemoteUserAuthenticator'

## The base URL of the entire application
c.JupyterHub.base_url = '/jupyter/'

## Whether to shutdown the proxy when the Hub shuts down.
#  
#  Disable if you want to be able to teardown the Hub while leaving the proxy
#  running.
#  
#  Only valid if the proxy was starting by the Hub process.
#  
#  If both this and cleanup_servers are False, sending SIGINT to the Hub will
#  only shutdown the Hub, leaving everything else running.
#  
#  The Hub should be able to resume from database state.
#c.JupyterHub.cleanup_proxy = True

## Whether to shutdown single-user servers when the Hub shuts down.
#  
#  Disable if you want to be able to teardown the Hub while leaving the single-
#  user servers running.
#  
#  If both this and cleanup_proxy are False, sending SIGINT to the Hub will only
#  shutdown the Hub, leaving everything else running.
#  
#  The Hub should be able to resume from database state.
#c.JupyterHub.cleanup_servers = True

## Maximum number of concurrent users that can be spawning at a time.
#  
#  Spawning lots of servers at the same time can cause performance problems for
#  the Hub or the underlying spawning system. Set this limit to prevent bursts of
#  logins from attempting to spawn too many servers at the same time.
#  
#  This does not limit the number of total running servers. See
#  active_server_limit for that.
#  
#  If more than this many users attempt to spawn at a time, their requests will
#  be rejected with a 429 error asking them to try again. Users will have to wait
#  for some of the spawning services to finish starting before they can start
#  their own.
#  
#  If set to 0, no limit is enforced.
#c.JupyterHub.concurrent_spawn_limit = 100

## The config file to load
c.JupyterHub.config_file = '/usr/local/jupyterhub/jupyterhub_config.py'

## File in which to store the cookie secret.
c.JupyterHub.cookie_secret_file = '/usr/local/jupyterhub/jupyterhub_cookie_secret'

## The location of jupyterhub data files (e.g. /usr/local/share/jupyter/hub)
#c.JupyterHub.data_files_path = '/usr/local/share/jupyter/hub'

## Include any kwargs to pass to the database connection. See
#  sqlalchemy.create_engine for details.
#c.JupyterHub.db_kwargs = {}

## url for the database. e.g. `sqlite:///jupyterhub.sqlite`
#c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'

## log all database transactions. This has A LOT of output
#c.JupyterHub.debug_db = False

## DEPRECATED since version 0.8: Use ConfigurableHTTPProxy.debug
#c.JupyterHub.debug_proxy = False

## Send JupyterHub's logs to this file.
#  
#  This will *only* include the logs of the Hub itself, not the logs of the proxy
#  or any single-user servers.
#c.JupyterHub.extra_log_file = ''

## Extra log handlers to set on JupyterHub logger
#c.JupyterHub.extra_log_handlers = []

## Generate default config file
#c.JupyterHub.generate_config = False

## The ip or hostname for proxies and spawners to use for connecting to the Hub.
#  
#  Use when the bind address (`hub_ip`) is 0.0.0.0 or otherwise different from
#  the connect address.
#  
#  Default: when `hub_ip` is 0.0.0.0, use `socket.gethostname()`, otherwise use
#  `hub_ip`.
#  
#  .. versionadded:: 0.8
#c.JupyterHub.hub_connect_ip = '127.0.0.1'

## The port for proxies & spawners to connect to the hub on.
#  
#  Used alongside `hub_connect_ip`
#  
#  .. versionadded:: 0.8
#c.JupyterHub.hub_connect_port = 0

## The ip address for the Hub process to *bind* to.
#  
#  See `hub_connect_ip` for cases where the bind and connect address should
#  differ.
c.JupyterHub.hub_ip = '0.0.0.0'

## The port for the Hub process
#c.JupyterHub.hub_port = 8081

## The public facing ip of the whole application (the proxy)
c.JupyterHub.ip = '127.0.0.1'

## Supply extra arguments that will be passed to Jinja environment.
#c.JupyterHub.jinja_environment_options = {}

## Interval (in seconds) at which to update last-activity timestamps.
#c.JupyterHub.last_activity_interval = 300

## Dict of 'group': ['usernames'] to load at startup.
#  
#  This strictly *adds* groups and users to groups.
#  
#  Loading one set of groups, then starting JupyterHub again with a different set
#  will not remove users or groups from previous launches. That must be done
#  through the API.
#c.JupyterHub.load_groups = {}

## Specify path to a logo image to override the Jupyter logo in the banner.
#c.JupyterHub.logo_file = ''

## File to write PID Useful for daemonizing jupyterhub.
c.JupyterHub.pid_file = '/usr/local/jupyterhub/server.pid'

## The public facing port of the proxy
#c.JupyterHub.port = 8000

## List of service specification dictionaries.
#  
#  A service
#  
#  For instance::
#  
#      services = [
#          {
#              'name': 'cull_idle',
#              'command': ['/path/to/cull_idle_servers.py'],
#          },
#          {
#              'name': 'formgrader',
#              'url': 'http://127.0.0.1:1234',
#              'api_token': 'super-secret',
#              'environment':
#          }
#      ]
#c.JupyterHub.services = []

## The class to use for spawning single-user servers.
#  
#  Should be a subclass of Spawner.
#c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'
#c.JupyterHub.spawner_class = 'sudospawner.SudoSpawner'
#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.JupyterHub.host_homedir_format_string = '/home/{username}'
#c.DockerSpawner.image = 'jupyter/scipy-notebook:8c465a3d72cb'
#c.DockerSpawner.hub_ip_connect = '192.168.172.1'
#c.Spawner.mem_limit = '2G'
#c.DockerSpawner.

##
## Sample configs copied.
##


# Spawn single-user servers as Docker containers
from dockerspawner import SystemUserSpawner

class MySystemUserSpawner(SystemUserSpawner):
    def get_env(self):
        env = super().get_env()
        env['COURSE_NAME'] = os.environ['COURSE_NAME']
        env['ADMIN_INSTRUCTOR_UID'] = os.environ['ADMIN_INSTRUCTOR_UID']
        env['INSTRUCTOR_GID'] = os.environ['INSTRUCTOR_GID']
        env['INSTRUCTOR_GROUP'] = os.environ['INSTRUCTOR_GROUP']
        env['COURSE_HOME_ON_CONTAINER'] = os.path.join('/home', self.user.name, os.environ['COURSE_NAME'])

        env['IS_INSTRUCTOR'] = 'false'
        for instructor in os.environ['INSTRUCTORS_LIST'].strip().split(','):
            if instructor.strip() == self.user.name:
                env['IS_INSTRUCTOR'] = 'true'

        return env

c.JupyterHub.spawner_class = MySystemUserSpawner

# Spawn containers from this image
c.DockerSpawner.image = os.environ['DOCKER_NOTEBOOK_IMAGE']

c.DockerSpawner.cmd = 'start-custom.sh'
# c.DockerSpawner.cmd = 'start-singleuser.sh'

# Connect containers to this Docker network
network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name

# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }


# Explicitly set notebook directory.
home_dir = '/home/{username}'
notebook_dir = home_dir
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
# c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir,'/home/shared':'/home/shared' }
c.DockerSpawner.volumes = {'/home/shared':'/home/shared',
        'nbgrader-exchange' : '/srv/nbgrader/exchange',
        os.environ['COURSE_HOME'] : '/srv/nbgrader/%s' % os.environ['COURSE_NAME']}
c.DockerSpawner.extra_create_kwargs.update({ 'volume_driver': 'local' })

# Remove containers once they are stopped
c.DockerSpawner.remove_containers = True

# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

## Additional configs for swarm?
c.DockerSpawner.host_ip = '0.0.0.0'
