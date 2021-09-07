from flask import Flask,render_template,request
import subprocess
  





app = Flask(__name__)
PORT = 4005

@app.route("/", methods =["GET","POST"])
def index():
	return render_template("index.html",title="Automate git push")






# getting input with name = Monday in HTML form 
@app.route('/getdetails', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        path=request.form.get("path")
        print(path)
        req_file = open("git.sh", "w")
        req_file.write(f'''#!/bin/sh
cd {path}
git add .
echo "added"
git commit -m "Updates for $(date +%F)"
echo "comitted"
git push  
echo "pushed"
        ''')
        req_file.close()
        subprocess.run("git.sh", shell=True, check=True)
    return render_template("added.html")
	



if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0", port=PORT)