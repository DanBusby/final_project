from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)
g = giphypop.Giphy()

def get_gif(responses):
    responses = g.search('cats')
    for response in responses:
        print(response.media_url)
        print(response.url)

   
@app.route('/')
def index():
    name = request.values.get('name', 'Nobody')
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    term = request.values.get('term')
    responses = get_gif(term)
    return render_template('results.html', responses=responses)

app.run(debug=True)