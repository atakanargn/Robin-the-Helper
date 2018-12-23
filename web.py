from flask import Flask
from flask import request
import robinSQL

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome sir!'

@app.route('/reply/<query>')
def reply(query):
    return "Robin said;\n"+robinSQL.reply(query)

@app.route('/cmd')
def cmd():
    robinSQL.curs.execute("SELECT * FROM querys")
    
    response = """<CENTER><TABLE  BORDER='2' WIDTH = '75%'>
   <TR>
      <TH COLSPAN='3'>
         <H3><BR>COMMANDS/DIALOGS</H3>
      </TH>
   </TR>
      <TH>Query</TH>
      <TH>Shell</TH>
      <TH>Answer</TH>
    """
    for satir in robinSQL.curs.fetchall():
        idd,query,shell,answer = satir[0],satir[1],satir[2],satir[3]
        response += "<TR><TD><A HREF='/reply/{}'>{}</A></TD><TD>{}</TD><TD>{}</TD></TR>".format(query,query,shell,answer)
    response += "</TABLE></CENTER>"
    return response