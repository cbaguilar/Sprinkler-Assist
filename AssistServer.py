#!/user/bin/python3
import json
from flask import Flask
from flask import request
import socket
app = Flask(__name__)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.2.70"
port = 42001

onOff = "False"

message  = '{"type":"direct","direct":{"sprinkler":1,"enabled":'+str(onOff)+'}}'



def checkOnOff(string):
    if "on" in string:
        return "true"
    else:
	return "false"

@app.route('/',methods=['POST'])
def display():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(request.data);
    postDataRaw = request.data


    postMessage = json.loads(postDataRaw)
    sprinklerNumber = postMessage["sprinkler"]-1
    onOff = str(checkOnOff(request.data))

    print("Sprinkler: "+str(sprinklerNumber))
    print("Turned " +postMessage["enabled"])

    message  = '{"type":"direct","direct":{"sprinkler":'+str(sprinklerNumber)+',"enabled":'+onOff+'}}'

    print("Sending Message: ")
    print(message)
    s.connect((host,port))
    s.send(message);
    s.close();
    return "Looks like it works!"

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=25565)





