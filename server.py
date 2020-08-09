from flask import Flask, render_template, request, redirect
import csv
# sets the name as the __main__
app = Flask(__name__)

# using render_template you need to create 
# templates folder and put html files inside it
@app.route('/')
def my_home():
    return render_template('portfolio.html')

@app.route('/<string:page_name>')
def landing_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\nEMAIL\n{email}\n,\nSUBJECT\n{subject}\n,\nMESSAGE\n{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer= csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return'did not save to database'
    else:
        return 'something went wrong' 
# @app.route('/components')
# def components():
#     return render_template('portfolio_components.html')

# @app.route('/<username>')
# def hello_world2(username=None):
#     return render_template('index.html', name=username)

# @app.route('/<username>/<int:post_id>')
# def hello_world3(username=None, post_id=None):
#     return render_template('index.html', name=username, post=post_id)

# @app.route('/blog')
# def blog():
#     return 'this are my thoughts'

# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'this is my dog'