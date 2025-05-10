from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
# print(__name__)

@app.route("/")
def myhome():
    return render_template('index.html')
# #
# @app.route("/works.html")
# def works():
#     # return ("<p>this is a blog i created</p>")
#     return render_template('works.html')
#
# @app.route("/about.html")
# def about():
#     # return ("<p>this is a blog i created</p>")
#     return render_template('about.html')
#
# @app.route("/contact")
# def contact():
#     # return ("<p>this is a blog i created</p>")
#     return render_template('contact.html')
#
# @app.route("/blog/dog")
# def blog2():
#     return ("<p>I write about dogs </p>")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        print(data)
        return redirect('thankyou.html')
    else:
        error = 'something went wrong, try again later'
    return render_template('contact.html', error=error)