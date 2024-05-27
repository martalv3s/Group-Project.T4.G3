from flask import Flask, render_template, request, session, redirect, url_for
from datafile import filename

import os

from classes.cliente import Cliente
from classes.pedido import Pedido
from classes.produto import Produto
from classes.userlogin import Userlogin

app = Flask(__name__)

Cliente.read(filename + 'business.db')
Pedido.read(filename + 'business.db')
Produto.read(filename + 'business.db')
Userlogin.read(filename + 'business.db')

prev_option = ""
submenu = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'fotos')
app.config['UPLOAD'] = upload_folder

import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_hform as gfhsub
import subs_subform as gfsubsub
import subs_customerFoto as customerfsub
import subs_mapaOrderform as mapasub
import subs_gform_pedido as gfsubP 
import subs_signup as ssub

@app.route("/signup")
def signup():
    return ssub.signup()

@app.route("/chkregister", methods=["post","get"])
def chkregister():
    return ssub.chkregister()

@app.route("/")
def index():
    print(session.get("user"))
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    global prev_option
    ulogin=session.get("user")
    uloginUp = session.get("up")
    print("Up login", uloginUp)
    if (ulogin != None):
        group = Userlogin.obj[ulogin].usergroup
        if group != "admin":
            Userlogin.current(ulogin)
            print("Up login", uloginUp)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = Userlogin.current()
            Userlogin.remove(obj.user)
            if not Userlogin.previous():
                Userlogin.first()
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            obj = Userlogin(request.form["user"],request.form["usergroup"], \
                            Userlogin.set_password(request.form["password"]))
            Userlogin.insert(obj.user)
            Userlogin.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Userlogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = Userlogin.set_password(request.form["password"])
                print(obj.password)
            Userlogin.update(obj.user)
        elif option == "first":
            Userlogin.first()
        elif option == "previous":
            Userlogin.previous()
        elif option == "next":
            Userlogin.nextrec()
        elif option == "last":
            Userlogin.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Userlogin.current()
        if option == 'insert' or len(Userlogin.lst) == 0:
            user = ""
            usergroup = ""
            password = ""
        else:
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, user=user,usergroup = usergroup,password=password, ulogin=session.get("user"), group=group)
    else:
        return render_template("index.html", ulogin=ulogin)

@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)

@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    return gfTsub.gformT(cname,submenu)

@app.route("/customer_foto", methods=["post","get"])
def gformFoto():
    cname = 'Produto'
    return customerfsub.customerFotoform(app,cname)

@app.route("/hform/<cname>", methods=["post","get"])
def hform(cname=''):
    submenu = request.args.get("subm")
    return gfhsub.hform(cname,submenu)
      
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    submenu = request.args.get("subm")
    return gfsubsub.subform(cname,submenu)

@app.route("/productform", methods=["post","get"])
def productFoto():
    submenu = request.args.get("subm")
    cname = 'Product'
    return productFotosub.productFoto(app,cname,submenu)

@app.route("/order/mapa", methods=["post","get"])
def ordermapa():
    submenu = request.args.get("subm")
    cname = ''
    return mapasub.mapaOrderform(app,cname,submenu)

@app.route("/uc", methods=["post","get"])
def uc():
    return render_template("uc.html", ulogin=session.get("user"),submenu=submenu)

@app.route("/gform_pedido/<cname>", methods=["post","get"])
def gform_pedido(cname=''):
    submenu = request.args.get("subm")
    return gfsubP.gform_pedido (cname,submenu)



if __name__ == '__main__':
    # app.run(debug=True,port=6001)
    
    app.run()