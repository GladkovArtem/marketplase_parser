from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from parser import models
from parser.models.database import db
from flask import redirect, url_for
from flask_login import current_user


class CustomView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))


class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for("auth.login"))
        return super(MyAdminIndexView, self).index()


admin = Admin(
    name="Parser Admin",
    index_view=MyAdminIndexView(),
    template_mode="bootstrap4"
)
#admin.add_view(CustomView(models.Tag, db.session, category="Models"))
admin.add_view(CustomView(models.Comment, db.session, category="Models"))


class TagAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True


admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))


class UserAdminView(CustomView):
    column_exclude_list = ("password",)
    column_searchable_list = ("first_name", "last_name", "username", "is_staff", "email")
    column_filters = ("first_name", "last_name", "username", "is_staff", "email")
    column_editable_list = ("first_name", "last_name", "is_staff")
    can_create = True
    can_edit = True
    can_delete = False


admin.add_view(UserAdminView(models.User, db.session, category="Models"))


class UrlAdminView(CustomView):
    column_searchable_list = ("link",)
    column_filters = ("link",)
    column_editable_list = ("link",)
    can_create = True
    can_edit = True
    can_delete = True


admin.add_view(UrlAdminView(models.Url, db.session, category="Models"))
