#User:Emmanuel Bamidele

from flask import Flask, request, render_template

app = Flask(__name__)

# This list will act as a temporary 'database' for stored posts
posts = []

class BlogPost:
    def __init__(self, title, content, author, publish_date):
        self.title = title
        self.content = content
        self.author = author
        self.publish_date = publish_date

    def __str__(self):
        return f"BlogPost(title={self.title}, author={self.author}, date={self.publish_date})"

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', posts=posts)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        publish_date = request.form['publish_date']
        
        new_post = BlogPost(title, content, author, publish_date)
        posts.append(new_post)
        return redirect(url_for('create_post'))  # Redirect back to the create post page
    return render_template('create_post.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

