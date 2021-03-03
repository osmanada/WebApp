from flask import Flask, render_template, url_for
app = Flask(__name__)

#dummy data
blogposts = [
	{
		"author": "Christopher",
		"title" : "Blog post 1",
		"content" : "First post content",
		"date_posted": "20th Jan 2021"

	},
	{
		"author": "Jhon",
		"title" : "Blog post 2",
		"content" : "First post content",
		"date_posted": "25th Jan 2021"

	},

]
@app.route('/')
def hello_world():
    return render_template("home.html", blogposts=blogposts)

@app.route('/about')
def about():
    return render_template("about.html", title = "About")


if __name__ == "__main__":
	app.run(debug=True)  #run flask in debug mode