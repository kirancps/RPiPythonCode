from flask import *
import time
from thing import *
app = Flask(__name__)
piThing=RPiThing()

@app.route("/")
def hello():
    sw=piThing.read_switch()
    return render_template("index.html", switch=sw)

@app.route("/led/<int:state>",methods=['POST'])
def led_state(state):
    if state == 1:
        piThing.set_led(True)
        #return "LED ON"
    elif state == 0:
        piThing.set_led(False)
        #return "LED OFF"
    else:
        return "Sorry, Try Something else"
    return ('', 204)
@app.route("/switch")
def switch():
    def read_switch():
        while True:
            switch = piThing.read_switch()
            yield 'data: {0}\n\n'.format(switch)
            time.sleep(1.0)
    return Response(read_switch(), mimetype='text/event-stream')

if __name__== "__main__":
    app.run(host='0.0.0.0',port=80, debug=True, threaded=True)
