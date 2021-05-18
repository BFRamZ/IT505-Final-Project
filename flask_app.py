from flask import Flask, flash, render_template, request, g, redirect
import db_manager
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'secret_key'

@app.before_first_request
def before_first_request():
    db_manager.create_table()
    pass
    
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/create_flight/", methods=['GET', 'POST'])
def create():
    if request.method=="GET":
        return render_template("create_flight.html")
    else: 
    
        pass_id = request.form.get('flight_id)
        source = request.form.get('source')
        destination = request.form.get('destination')
        flight_time = request.form.get('flight_time')
        num_seats = request.form.get('num_seats')
        
        status = db_manager.create_flight(flight_id, source, destination, flight_time, num_seats)
        
        rows = db_manager.select_all()
    
        if "success" in status:
            flash(status)
            return redirect(f"/update/{flight_id}")
        
        else:
            flash(status)
            return redirect('/create_flight/')
        
@app.route("/create_passenger/", methods=['GET', 'POST'])
def create():
    if request.method=="GET":
        return render_template("create_passenger.html")
    else: 
    
        pass_id = request.form.get('pass_id)
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        seat_level = request.form.get('seat_level')
        seat_number = request.form.get('seat_number')
        
        status = db_manager.create_passenger(pass_id, first_name, last_name, seat_level, seat_number)
        
        rows = db_manager.select_all()
    
        if "success" in status:
            flash(status)
            return redirect(f"/update/{pass_id}")
        
        else:
            flash(status)
            return redirect('/create_passenger/')

@app.route("/update/<pass_id>", methods=['GET','POST'])
def update(pass_id):
    if request.method == "GET":
        the_pass = db_manager.select_by_pass_id(pass_id)
        
        return render_template('create_passenger.html', passenger = the_pass)
    
    else:
        first_name = (request.form['first_name'])
        last_name = (request.form['last_name'])
        seat_level = (request.form['seat_level'])
        seat_number = (request.form['seat_number'])
        
    
        status = db_manager.update_passenger(first_name, last_name, seat_level, seat_number, pass_id)
        
        flash(status)
        return redirect(f'/update/{passenger_id}')

@app.route("/update/<pass_id>", methods=['GET','POST'])
def update(pass_id):
    if request.method == "GET":
        the_pass = db_manager.select_by_pass_id(pass_id)
        
        return render_template('create_passenger.html', passenger = the_pass)
    
    else:
        first_name = (request.form['first_name'])
        last_name = (request.form['last_name'])
        seat_level = (request.form['seat_level'])
        seat_number = (request.form['seat_number'])
        
    
        status = db_manager.update_passenger(first_name, last_name, seat_level, seat_number, pass_id)
        
        flash(status)
        return redirect(f'/update/{passenger_id}')

@app.route("/delete/<car_id>")
def delete(car_id):
    status = db_manager.delete_car(car_id)
    return redirect(request.referrer)

@app.route("/list/")
def listing():
    rows = db_manager.select_all()   
    return render_template("list.html", cars=rows)
    
@app.route('/reset/')
def reset():
    db_manager.reset_database()
    flash('database reset')
    
    return redirect('/')

# @app.route('/search', methods=["GET", "POST"])
# def search():
#     if request.method=="GET":
#         return render_template("search.html")
#     else:
#         args = {}
#         for key, val in request.form.items():
#             if val:
#                 args[key]=val
#         rows=db_manager.select(args)
#         return render_template("list.html", cars=rows)
    
# @app.route("/browse/")
# @app.route("/browse/<make>/<model>")
# def browse(make=None, model=None):
#     if not make and not model:
#         makes = db_manager.get_makes()
#         makes = [make[0] for make in makes]
#         models = []
#         for make in makes:
#             rows = db_manager.get_models(make)
#             rows = [row[0] for row in rows]
#             models.append(rows)
#             the_data = {'makes':makes, 'models':models}
#         return render_template("browse.html", data=the_data)
#     else:
#         rows = db_manager.select({'make':make, 'model':model})
#         return render_template("list.html",cars=rows)
    
# @app.route('/import', methods=["GET", "POST"])
# def import_data():
#     if request.method=="GET":
#         return render_template("import.html")
#     else:
#         f = request.files["myfile"]
#         filename = secure_filename(f.filename)
#         f.save(os.path.join('uploads', filename))
#         status = db_manager.load_csv(os.path.join('uploads', filename))
#         flash(status)
#         return redirect('/')