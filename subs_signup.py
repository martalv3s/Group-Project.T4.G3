from flask import render_template, request, session
from classes.userlogin import Userlogin

def signup():
    return render_template("signup.html", user="", usergroup="", password="", up ="", ulogin=session.get("user"), resul="")

def chkregister():
    user = request.form["user"]
    usergroup = request.form["usergroup"]
    password = request.form["password"]
    up = request.form["up"]
    x = Userlogin.check(up)
    if user in Userlogin.obj:
        k = "User já existe."
        return render_template("signup.html", user=user, usergroup=usergroup, password=password, up = up, ulogin=session.get("user"), resul=k)
    elif x == "Válido":
        new_user = Userlogin(user, usergroup, Userlogin.set_password(password), up)
        Userlogin.obj[user] = new_user
        Userlogin.insert(user)
        Userlogin.lst.append(user)
        resul = "Registration successful."
        
        session["user"] = user
        session["usergroup"] = usergroup
        
        return render_template("signup.html", ulogin=session.get("user"), usergroup=session.get('usergroup'))
    else:
        return render_template("signup.html", user = user, usergroup = usergroup, password = password, up = up, ulogin = session.get("user"), resul = x)