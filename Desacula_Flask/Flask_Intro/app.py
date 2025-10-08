from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/uppercase', methods=['GET', 'POST'])
def uppercase():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        result = text.upper()
    return render_template('uppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    if request.method == 'POST':
        radius = float(request.form['radius'])
        area = 3.1416 * radius * radius
        return render_template('area_circle.html', area=area, radius=radius)
    return render_template('area_circle.html')

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        area = 0.5 * base * height
        return render_template('area_triangle.html', area=area, base=base, height=height)
    return render_template('area_triangle.html')

if __name__ == '__main__':
    app.run(debug=True)
