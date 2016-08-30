from restsrv import app
from restsrv.config import config


if __name__ == "__main__":
    restsrv_host = config.get('restsrv', 'host')
    restsrv_port = config.get('restsrv', 'port')
    app.run(host=restsrv_host, port=restsrv_port, threaded=True)