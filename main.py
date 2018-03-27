from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""


form = """
    <head>
        <style>
        form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
       <form method='post'>
       Rotate by: 
       <input type="text" name="rot" id="rot"  value="0"/> <br>
       <textarea  name="text">{0} </textarea><br>
       <input type="submit" value="Submit Query"/>
       </form>
    </body>
</html>  """
@app.route("/", methods=['POST'])
def encrypt():
    text_encrypt = request.form['text']
    rot_encrypt = int(request.form['rot'])

    rotation = rotate_string(text_encrypt,rot_encrypt)
    content =  rotation 
    return form.format(content)


@app.route("/")
def index():
    return form.format("")

app.run()    