from flask import Blueprint, render_template,request, redirect, url_for, flash

users = Blueprint("users", __name__)
user_details=[{"User.name":"Pallavi", "Password":"123"}]


@users.route("/users/login", methods=["GET","POST"])
def users_profile():
    print(request.method)
    if request.method=="POST":
        form_data=request.form_data
        user_name=form_data.get("fname")
        password=form_data.get("password")

        # Check if provided user_name and password match any user in user_details
        for user in user_details:
            if user_name==user["User_name"] and password==user["Password"]:
                return render_template("users/profile.html")

        # If the login credentials are not valid, show on error message or redirect to the login page
        error_message="Invalid login credentials. Please try again."
        return render_template("users/login.html",error_message=error_message)
    
    return render_template("users/login.html")

@users.route("/users/register", methods=["GET","POST"])
def users_registration():
    print(request.method)
    if request.method=="POST":
        form_data=request.form
        user_name=form_data.get("username")
        password=form_data.get("password")

        user_details.append({"User_name": user_name, "Password" : Password})
        
    
        return redirect(url_for("users.users_login"))
    else:
        return render_template("users/register.html")
