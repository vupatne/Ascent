from flask import Blueprint,request,jsonify, render_template, session
from utils.protectInjection import checkInjection
from repository.users import getuserByPhoneAndPassword

signin = Blueprint('signin', __name__)


@signin.route('/', methods=['GET'])
def login_click():
    session.pop('userid', None)
    return render_template("signin.html",)


@signin.route('/signin', methods=['POST', 'GET'])
def signin_submit():
    if request.method == 'POST':
        data = request.form
        if checkInjection(data):
            return jsonify({"msg": "injection"})

        phone = data["phone"]
        password = data["idpassword"]

        res_user = getuserByPhoneAndPassword(phone, password)
        if len(res_user) == 0:
            return render_template("signin.html", response2='error', msg="You are not a user.")

        user = res_user[0]
        session['userid'] = user[1]
    return render_template("selectaction.html")

@signin.route('/action', methods=['GET'])
def select_action():
    return render_template("selectaction.html",)