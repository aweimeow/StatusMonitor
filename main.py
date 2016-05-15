from flask import Flask, request, redirect

from core.token import load_token
from core.system import getIP

app = Flask('statuslook')
HOST = getIP('eth0')
PORT = 5678
TOKEN = load_token()


@app.route('/%s' % TOKEN)
def web():
    return '%s' % TOKEN

if __name__ == '__main__':
    print('TOKEN: %s' % TOKEN)
    app.run(host=HOST, port=PORT)
