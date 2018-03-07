from flask import Flask, redirect, url_for, request,render_template,flash
from flask_sqlalchemy import SQLAlchemy
import pyodbc
#import urllib
app = Flask(__name__)
app.secret_key = "ampashyampakirikiri"
#params = urllib.quote_plus("DRIVER={ODBC Driver 13 for SQL Server};SERVER=imagineproject.database.windows.net;DATABASE=bagIT;UID=saitejagudapati;PWD=Nasaisro123@95")

#engine = SQLAlchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://saitejagudapati:Nasaisro123@95@imagineproject.database.windows.net/bagIT?driver=ODBC+Driver+13+for+SQL+Server'
#db = SQLAlchemy(app)
server = 'imagineproject.database.windows.net'
database = 'bagIT'
username = 'saitejagudapati'
password = 'Nasaisro123@95'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cur = cnxn.cursor()
@app.route('/success/<airline>')
def success(airline):
    return 'welcome %s' % airline
"""class bittable(db.Model):
    airline = db.Column('airline',db.String(10), primary_key = True)
    flight_number = db.column('flight_number',db.String(50))
    bitbox = db.column('bitbox',db.String(10))
    def __init__(self,airline,flight,bitbox):        
        self.airline = airline
        self.flight_number = flight
        self.bitbox = bitbox"""
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      airline = request.form['airline']
      flight_number = request.form['flight_number']
      bitbox = request.form['bitid']
      #bittab = bittable(airline,flight_number,bitbox)
      #que1 = bittab.query.filter_by(airline = airline,flight_number = flight_number).first()
      #que1.bitbox = request.form['bitid']
      #db.session.commit()
      query = "Update dbo.bittable  Set bitbox = '%s' Where airline = '%s' and flight_number = '%s'"%(bitbox,airline,flight_number)
      cur.execute(query)
      cnxn.commit()
      return render_template('alloted.html', airline = airline, flight = flight_number, bitid = bitbox)
   else:
      airline = request.args.get('airline')
      return redirect(url_for('success',airline = airline))

if __name__ == '__main__':
   app.run(debug = True)
