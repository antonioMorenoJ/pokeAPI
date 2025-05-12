import sys

from aps.settings import settings
#from src.app import app
from src.app import app
########################################################################################################################
#  Run the app
########################################################################################################################


if __name__ == '__main__':
    args = sys.argv[1:]

    if not args:
        app.debug = settings.DEBUG_MODE
        app.run(threaded=True)

    else:
        port = None
        host = None
        debug = settings.DEBUG_MODE
        for arg in args:
            if arg[:7] == '--port=':
                port = int(arg[7:])
            elif arg[:8] == '--debug=':
                debug = arg[8:] == 'True'
            elif arg[:7] == '--host=':
                host = arg[7:]
        app.run(host=host, port=port, debug=debug, threaded=True)

#export FLASK_ENV=development