from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
       <form method='post'>
       Rotate by: 
       <input type="text" name="rot" id="rot"  value="0"/> <br>
       <textarea  rows = "200" cols = "400" name="text" > </textarea><br>
       <input type="submit" value="Submit Query"/>
       </form>
    </body>
</html>

"""
@app.route("/", methods=['POST'])
def encrypt():
    text_encrypt = request.form['text']
    
    rotation = rotate_string(text_encrypt)
    web_encrypt_element = "<h1>" + rotation + "</h1>"

    return web_encrypt_element

@app.route("/")
def index():
    encrypted_mesg = encrypt()
    return encrypted_mesg

app.run()    