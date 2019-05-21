from flask import *
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import time
rc=[]
rcb=[]
laun=[]
launb=[]
plum=[]
plumb=[]
elec=[]
elecb=[]
l=[]
lb=[]
e=0



app = Flask(__name__,template_folder='./')
from datetime import *
exp=''

@app.route('/', methods=['POST', 'GET'])
def my_form():
	if request.method=="POST":
	    opt=request.form['option']
	    if opt=="facility":
	        return redirect("form.html")
	    elif opt=="security":
	        return redirect("firstpage1.html")
	return render_template("main.html")

@app.route('/form.html',methods=['GET','POST'])
def my_form_role():
    if request.method == 'POST':
        role = request.form['role']
        if role=="Student":
            return redirect("form2.html")
        elif role=="Worker":
            return redirect("form3.html")
    return render_template("form.html")
        
@app.route('/form3.html', methods=['GET', 'POST'])
def my_form_exp():
    global e
    if request.method == 'POST':
        ex=request.form['exp']
        if ex=="rc":
            e=1
        elif ex=="laun":
            e=2
        elif ex=="elec":
            e=4
            
        return redirect("form5.html")
    return render_template("form3.html")

@app.route('/form2.html', methods=['GET', 'POST'])
def my_form_work():
    global l
    global lb
    if request.method == 'POST':
        work=request.form["work"]
        if work=="rc":
            l=rc
            lb=rcb
        elif work=='laun':
            l=laun
            lb=launb
        elif work=="elec":
            l=elec
            lb=elecb
            
        return redirect("form4.html")
    return render_template("form2.html")

@app.route('/form4.html', methods=['GET', 'POST'])
def my_form_slot():
    global l
    global lb
    if request.method=="POST":
        slot=request.form["slot"]
        if slot in l:
            lb.append(slot)
            l.remove(slot)
            return "Slot booked"
        else:
            return "Slot not available"
    return render_template("form4.html")

@app.route('/form5.html', methods=['GET', 'POST'])
def my_form_sched():
    if request.method=="POST":
        sched=request.form["sched"]
        sched=sched.split()
        if e==1:
            global rc
            rc=sched
        elif e==2:
            global laun
            laun=sched
        elif e==4:
            global elec
            elec=sched
        return redirect('/form.html')
    return render_template("form5.html")

@app.route('/firstpage1.html', methods=['GET', 'POST'])
def secondpage():
	if request.method=="POST":
		n=request.form['n']
		checkout =date.today() + timedelta(days=int(n))
		strform = checkout.strftime('%Y-%m-%d')
		t = datetime.time(datetime.now())
		a=str(t)
		comp=a[:5]
		if int(n)==0:
			return redirect('secondpage1.html')
		else:
			return redirect('firstpage1.html')
	return render_template('firstpage1.html')

@app.route('/secondpage1.html', methods=['GET', 'POST'])
def thirdpage():
	if request.method=="POST":
		global exp
		exp=request.form['exp']
		return redirect("secondpage2.html")
	return render_template("secondpage1.html")

@app.route('/secondpage2.html', methods=['GET', 'POST'])
def fourthpage():
	if request.method == 'POST':
		global exp
		reach=request.form['reach']
		#REFRESH

		t = datetime.time(datetime.now())
		a=str(t)
		comp=a[:5]
			
		flag=-1
		if int(comp[0:2])==int(exp[0:2]):
			
			#time.sleep(60)
			if int(comp[3:])>=int(exp[3:]) and int(comp[3:])<=(int(exp[3:])+1):
				print(reach)
				if reach=='y':
					flag=2

					MY_ADDRESS = "abcd@xyz.com"	#write SENDER'S email address here
					PASSWORD = 'password'		#write password of Sender
		   
					s = smtplib.SMTP(host='smtp.gmail.com', port=587)
					s.starttls()
					s.login(MY_ADDRESS, PASSWORD)


					msg = MIMEMultipart()       


					message = "NAME OF THE STUDENT- heya0890. The student has reached on time in the campus."

					    # setup the parameters of the message
					msg['From']=MY_ADDRESS
					msg['To']="xxx@yyy.com"		#enter reciever's email address
					msg['Subject']="returned"	#subject of the email
					        
					    # add in the message body
					msg.attach(MIMEText(message, 'plain'))
					        
					    # send the message via the server set up earlier.
					s.send_message(msg)
					del msg
					        
					    # Terminate the SMTP session and close the connection
					s.quit()
				
					return redirect("firstpage1.html")

				elif reach.strip()=='n':
					return redirect("secondpage1.html")
				else:

					MY_ADDRESS = "abcd@xyz.com"		#enter reciever's email address
					PASSWORD = 'password'			#write password of Sender
		   
					s = smtplib.SMTP(host='smtp.gmail.com', port=587)
					s.starttls()
					s.login(MY_ADDRESS, PASSWORD)


					msg = MIMEMultipart()       


					message = "NAME OF THE STUDENT- heya0890. The student has reached on time in the campus."

					    # setup the parameters of the message
					msg['From']=MY_ADDRESS
					msg['To']="xxx@yyy.com"			#enter reciever's email address
					msg['Subject']="returned"		#subject of the email
					        
					    # add in the message body
					msg.attach(MIMEText(message, 'plain'))
					        
					    # send the message via the server set up earlier.
					s.send_message(msg)
					del msg
					        
					    # Terminate the SMTP session and close the connection
					s.quit()
					
					return redirect("firstpage1.html")
	return render_template("secondpage2.html")

if __name__=="__main__":
	app.run(debug=True);
