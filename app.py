import os

from flask import Flask, redirect, render_template, request, session, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
from thirdweb import ThirdwebSDK

from flask_session import Session

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
NFT_COLLECTION_ADDRESS = "0xdc024d592D197053BdEcB966121C323A846EF1a5"
TOKEN_ID = 0

sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, "mumbai")
contract = sdk.get_edition_drop(NFT_COLLECTION_ADDRESS)

# Initialize Flask app
app = Flask(__name__)

# Configure Flask app
app.config['SECRET_KEY'] = 'secret'
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

socketio = SocketIO(app, manage_session=False)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/connect", methods=["POST", "GET"])
def connect():

    # User submitting form via POST
    if request.method == "POST":
      try:
        userWallet = request.form.get("address")
        balance = contract.balance_of(userWallet, TOKEN_ID)
      except TypeError:
        print("Invalid address")

        #TODO: render a 404 page
        return False

      userWallet = request.form.get("address")
      username = request.form.get("username")
      balance = contract.balance_of(userWallet, TOKEN_ID)

      # Store username in session
      session['username'] = username

      # User has not minted the NFT = not registered
      if not balance:
          print("Has YET to get the NFT checked")
          return render_template("mint.html")
      else:
          return render_template("exclusive.html", session=session)

    # User reached route via GET
    else:
        return render_template("connect.html")

@app.route("/mint")
def mint():
    return render_template("mint.html")

@app.route("/exclusive")
def displayExclusiveContent():
    return render_template("exclusive.html")


@socketio.on('join', namespace='/connect')
def join(message):
    room = "Exclusive Chatroom"
    join_room(room)
    emit('status', {'msg':  session.get('username') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/connect')
def text(message):
    room = "Exclusive Chatroom"
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/connect')
def left(message):
    room = "Exclusive Chatroom"
    username = session.get("username")
    leave_room(room)
    session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)

if __name__ == "__main__":
  socketio.run(app)