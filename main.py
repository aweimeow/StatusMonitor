import json
from flask import Flask, Response

from core.token import load_token
from core.system import getIP
import lib.cpu
import lib.memory

app = Flask('statuslook')
HOST = getIP('eth0')
PORT = 5678
TOKEN = load_token()

app.debug = True


@app.route('/%s/cpu/<func>' % TOKEN)
def cpu(func):
    result = getattr(lib.cpu, func)()
    return Response(json.dumps(result), mimetype='application/json')

@app.route('/%s/memory/<func>' % TOKEN)
def memory(func):
    result = getattr(lib.memory, func)()
    return Response(json.dumps(result), mimetype='application/json')


if __name__ == '__main__':
    print('TOKEN: %s' % TOKEN)
    app.run(host=HOST, port=PORT)
