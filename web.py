import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)
g = giphypop.Giphy()


# def get_gif(term):
#     responses = g.search(term)
#     # for response in responses:
#     #     return(response.media_url)
#     #     return(response.url)
  
@app.route('/')
def index():
    name = request.values.get('name', 'You Sexy Beast')
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    term = request.values.get('term') 
    responses = g.search(term)
    reply = 'GIFs tagged with "{}"'.format(term)
    return render_template('results.html', responses=responses, reply=reply)

# @app.route('/results')
# def results():
#     term = request.values.get('term')
#     reply = "GIFs tagged with {}".format(term)
#     responses = get_gif(term)
#     return render_template('results.html', responses=responses, reply=reply)

# app.run(debug=True)
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)