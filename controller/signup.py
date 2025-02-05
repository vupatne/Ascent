from flask import Blueprint,request,jsonify, render_template
from utils.protectInjection import checkInjection
from repository.users import getuserByPhoneWithoutFlag, add_user

signup = Blueprint('signup', __name__)


@signup.route('/getsignup', methods=['GET'])
def get_signup():
    return render_template("signup.html",)


@signup.route('/signup', methods=['POST'])
def signup_submit():
    if request.method == 'POST':
        data = request.form
        if checkInjection(data):
            return jsonify({"msg": "injection"})

        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        phone = str(data["phonenumber"])
        address = data["address"]
        reference = data["reference"]
        password = data["idpassword"]

        try:
            # If user is already present for phone number
            res_user = getuserByPhoneWithoutFlag(phone)
            if len(res_user) > 0:
                return render_template("signup.html", response2='error',
                                       msg="User is already present with phone number.")

            add_user(firstname, lastname, email, phone, address, reference, password)
            return render_template("signup.html", response2='success',
                                   msg="Your registration is sucessfull.")

        except Exception as e:
            print(e)
            return render_template("signup.html", response2='error', msg=str(e))