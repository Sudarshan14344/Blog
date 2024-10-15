ECHO is on.
from flask import Flask , jsonify , request, render_template
from models import db, BlogPost

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

#To create a new Blog Post
@app.route('/posts', methods = ['Post'])
def create_post():
    data = request.get_jsonify()
    new_post = BlogPost(title = data['title'], content = data['content'])
    db.session.add(new_post)
    db.session.commit()
    retuen jsonify ({'message': 'Post created successfully!'}),201

#To get Blog Post 
@app.route('/posts', methods = ['GET'])
def get_post():
    posts = BlogPost.query.all()
    return jsonify([{'id' : post.id , 'title': post.title, 'content': post.content} for post in posts])

#To update Blog posts
@app.route('/posts/<int:post_id>', methods = ['PUT'])
def update_post(post_id):
    data = request.get_jsonify()
    post = BlogPost.query.get_or_404(post_id)
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify ({'message': 'Post updated successfully!'})

#To delete Blog Post
@app.route('/posts/<int:post_id>', methods = ['DELETE'])
def delete_post(post_id):
    return jsonify({'message': 'Post deleted successfully!'})



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
