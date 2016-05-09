from flask import render_template, session, redirect, url_for, current_app, request, flash
from .. import db
from ..models import User, Post
from . import main
from .forms import NameForm, PostForm
from flask.ext.login import login_required, current_user


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('index.html',
                           posts = posts, pagination=pagination)


@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', posts=[post])


@main.route('/edit_post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit(): 
        post = Post(id=post.id, body=form.body.data, article_name=form.title.data,
                    author_id=5)
        db.session.merge(post)
        db.session.commit()
        flash('The post has been updated.')
        return redirect(url_for('.post', id=post.id))
    form.body.data = post.body
    return render_template('edit.html', form=form)


@main.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = PostForm()
    if form.validate_on_submit(): 
        post = Post(body=form.body.data, article_name=form.title.data,
                    author_id=5)
        db.session.add(post)
        db.session.commit()
        flash('The post has been updated.')
        return redirect(url_for('.post', id=post.id))
    return render_template('edit.html', form=form)


@main.route('/code')
def code():
    pass


@main.route('/music')
def music():
    pass


@main.route('/novel')
def novel():
    pass
