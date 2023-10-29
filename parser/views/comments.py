from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound
from parser.models.database import db
from parser.models import User, Comment, Tag
from parser.forms.comment import CreateCommentForm


comments_app = Blueprint("comments_app", __name__)


@comments_app.route("/", endpoint="list")
def comments_list():
    comments = Comment.query.all()
    return render_template("comments/list.html", comments=comments)


@comments_app.route("/<int:comment_id>/", endpoint="details")
def comment_details(comment_id):
    comment = Comment.query.filter_by(id=comment_id).options(
        joinedload(Comment.tag)
    ).one_or_none()
    if comment is None:
        raise NotFound
    return render_template("comments/details.html", comment=comment)


@comments_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_comment():
    error = None
    form = CreateCommentForm(request.form)
    form.tag.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():
        comment = Comment(title=form.title.data.strip(), body=form.body.data)
        db.session.add(comment)
        if form.tag.data:
            selected_tag = Tag.query.filter(Tag.id.in_(form.tag.data))
            for tag in selected_tag:
                comment.tag.append(tag)
        if current_user:
            comment.user = current_user
        else:
            user = current_user
            db.session.add(user)
            db.session.flush()
            comment.user = current_user.username
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new comment!")
            error = "Could not create comment!"
        else:
            return redirect(url_for("comments_app.details", comment_id=comment.id))
    return render_template("comments/create.html", form=form, error=error)
