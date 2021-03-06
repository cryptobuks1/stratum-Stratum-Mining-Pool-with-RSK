'''
This is example configuration for Stratum server.
Please rename it to config.py and fill correct values.
'''

# ******************** GENERAL SETTINGS ***************

# Enable some verbose debug (logging requests and responses).
DEBUG = False

# Destination for application logs, files rotated once per day.
LOGDIR = 'log/'

# Main application log file.
LOGFILE = 'stratum.log'

# Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGLEVEL = 'DEBUG'

# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 200

ENABLE_EXAMPLE_SERVICE = True

# ******************** TRANSPORTS *********************

# Hostname or external IP to expose
HOSTNAME = 'localhost'

# Port used for Socket transport. Use 'None' for disabling the transport.
LISTEN_SOCKET_TRANSPORT = 3333

# Port used for HTTP Poll transport. Use 'None' for disabling the transport
LISTEN_HTTP_TRANSPORT = None

# Port used for HTTPS Poll transport
LISTEN_HTTPS_TRANSPORT = None

# Port used for WebSocket transport, 'None' for disabling WS
LISTEN_WS_TRANSPORT = None

# Port used for secure WebSocket, 'None' for disabling WSS
LISTEN_WSS_TRANSPORT = None

# Hostname and credentials for one trusted Bitcoin node ("Satoshi's client").
# Stratum uses both P2P port (which is 8333 already) and RPC port
BITCOIN_TRUSTED_HOST = 'localhost'
BITCOIN_TRUSTED_PORT = 32592
BITCOIN_TRUSTED_USER = 'admin'
BITCOIN_TRUSTED_PASSWORD = 'admin'

# Hostname and credentials for one trusted RSK node.
RSK_TRUSTED_HOST = 'localhost'
RSK_TRUSTED_PORT = 4444
RSK_TRUSTED_USER = 'admin'
RSK_TRUSTED_PASSWORD = 'admin'
RSK_POLL_PERIOD = 2
RSK_NOTIFY_POLICY = 2

# Use this settings ONLY for development
RSK_DEV_MODE = False
RSK_DEV_TARGET = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
BTC_DEV_TARGET = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
RSK_STRATUM_DIFFICULTY = 0.01

# Use "echo -n '<yourpassword>' | sha256sum | cut -f1 -d' ' "
# for calculating SHA256 of your preferred password
ADMIN_PASSWORD_SHA256 = '84559e0732fad578fd9ddabb60a611880fe5579dbc600a7312ca0405a332da9b'
#ADMIN_PASSWORD_SHA256 = '9e6c0c1db1e0dfb3fa5159deb4ecd9715b3c8cd6b06bd4a3ad77e9a8c5694219' # SHA256 of the password

IRC_NICK = None

'''
DATABASE_DRIVER = 'MySQLdb'
DATABASE_HOST = 'localhost'
DATABASE_DBNAME = 'pooldb'
DATABASE_USER = 'pooldb'
DATABASE_PASSWORD = '**empty**'
'''

# Pool related settings
INSTANCE_ID = 31
# Change this setting for a valid address from BTC
CENTRAL_WALLET = 'mgjPZrmmpAVuetUBbokcaEm9uZqVAUFvAu'
PREVHASH_REFRESH_INTERVAL = 30 # in sec
MERKLE_REFRESH_INTERVAL = 60 # How often check memorypool
COINBASE_EXTRAS = '/rsk_stratum/'
