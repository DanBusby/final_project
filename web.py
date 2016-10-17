import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)
g = giphypop.Giphy()

#Displays the greeting when a user goes to the index page
@app.route('/')
def index():
    name = request.values.get('name', 'You Sexy Beast') #Builds confidence of user
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting=greeting)

#Routes user from index page to about page
@app.route('/about')
def about():
    return render_template('about.html')

#Routes user from index to results page once a user has submitted a search term
@app.route('/results')
def results():
    term = request.values.get('term') 
    responses = g.search(term)
    reply = 'GIFs tagged with "{}"'.format(term) #Customizes response based on search term
    return render_template('results.html', responses=responses, reply=reply)

#Code to push to Heroku
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)