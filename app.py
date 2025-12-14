from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from models import db, Contact

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# 仮ユーザー（後でDBにする）
class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# ---------- 公開ページ ----------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        contact = Contact(
            name=name,
            email=email,
            message=message
        )
        db.session.add(contact)
        db.session.commit()

        return redirect(url_for("contact"))

    return render_template("contact.html")



# ---------- 認証 ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User(1)
        login_user(user)
        return redirect(url_for("admin_dashboard"))
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# ---------- 管理画面 ----------
@app.route("/admin")
@login_required
def admin_dashboard():
    return render_template("admin/dashboard.html")


@app.route("/admin/contacts")
@login_required
def admin_contacts():
    contacts = Contact.query.order_by(Contact.created_at.desc()).all()
    return render_template("admin/contacts.html", contacts=contacts)


@app.route("/admin/contacts/<int:id>", methods=["GET", "POST"])
@login_required
def admin_contact_detail(id):
    contact = Contact.query.get_or_404(id)

    if request.method == "POST":
        contact.status = request.form["status"]
        db.session.commit()
        return redirect(url_for("admin_contacts"))

    return render_template("admin/contact_detail.html", contact=contact)


@app.route("/admin/contacts/<int:id>/delete", methods=["POST"])
@login_required
def admin_contact_delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for("admin_contacts"))



with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
