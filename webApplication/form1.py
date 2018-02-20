from flask import Flask ,redirect,url_for ,  request
app=Flask(__name__)



@app.route('/success/<name>')
def success(name):
    return "submit successfully"

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method=='POST':
        #fn=request.form['firstName']
        user=request.form['lastName']
        return redirect(url_for('success',name=user))
    else :
        return "sorry try again"
if __name__=='__main__':
    app.run()
