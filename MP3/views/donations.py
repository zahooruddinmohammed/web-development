from datetime import datetime, timedelta
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
donations = Blueprint('donations', __name__, url_prefix='/donations')
import re

@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve donation id as id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments, organization_name using a LEFT JOIN
    query = """SELECT A.id, first_name, last_name, email, organization.organization_id, item_name, item_description, item_quantity, donation_date, comments, organizaions.name AS organization_name
     FROM donations LEFT JOIN organizations ON donations.organization_id = organizations.organization_id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "organization_name" ,"item_name", "item_quantity", "created", "modified"]
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    # TODO search-3 append like filter for donor_firstname if provided
    # TODO search-4 append like filter for donor_lastname if provided
    # TODO search-5 append like filter for donor_email if provided
    # TODO search-6 append like filter for item_name if provided
    # TODO search-7 append equality filter for organization_id if provided
    # TODO search-8 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # TODO search-9 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-10 provide a proper error message if limit isn't a number or if it's out of bounds
    #zm254-10/18/23
    filters= [("fn","first_name"),("ln","last_name"),("email","email")]
    for filter_arg,filter in filters:
        if request.args.get(filter_arg):
            query += f" and {filter} like %(filter_{filter_arg})s"
            args[f"filter_{filter_arg}"]= f"%{request.args.get(filter_arg)}%"
    
    if request.args.get("organization"):
        query += f" and organization_id=%(organization_id)s"
        args["organization_id"]= request.args.get("organization")

    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns  and request.args.get("order") in ["asc","desc"]:
            query += f" ORDER BY {request.args.get('column')}{request.args.get('order')}"
    #zm254-10/18/23


    
    limit = 10 # TODO change this per the above requirements
    query += " LIMIT %(limit)s"
    
    ql= int(request.args.get('limit',10))
    if ql<1 or ql>100:
        flash("Limit values should be in the range of 1-100; Defaulting to 10")
        args["limit"]=10
    else:
        args["limit"]=ql 

    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            #print(f"rows: {rows}")
    except Exception as e:
        # TODO search-11 make message user friendly
        #zahooruddin zohaib mohammed-11-18-23
        print(e)
        flash(f"Unexpected error while trying to search employee: {e}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    # TODO search-12 if request args has organization identifier set organization_name variable to the correct name
    if request.args.get("organization"):
        try:
            result = DB.selectOne("SELECT name FROM organizations WHERE id = %(organization_id)s",
                      {"organization_id": request.args.get("organization")})

            if result.status:
                organization_name = result.row["name"]
        except Exception as e:
            flash("An error occured while retriveing organization name.Please try again later.","error")

    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns)


@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
        # TODO add-2 donor_firstname is required (flash proper error message)
        # TODO add-3 donor_lastname is required (flash proper error message)
        # TODO add-4 donor_email is required (flash proper error message)
        # TODO add-4a email must be in proper format (flash proper message)
        # TODO add-5 organization_id is required (flash proper error message)
        # TODO add-6 item_name is required (flash proper error message)
        # TODO add-7 item_description is optional
        # TODO add-8 item_quantity is required and must be more than 0 (flash proper error message)
        # TODO add-9 donation_date is required and must be within the past 30 days
        # TODO add-10 comments are optional
        form_value = {}
        has_error = False # use this to control whether or not an insert occurs

        form_value["donor_firstname"] = input.getlist("donor_firstname")
        form_value["donor_lastname"] = input.getlist("donor_lastname")
        form_value["donor_email"] = input.getlist("donor_email")
        form_value["organization_id"]= input.getlist("organization_id")
        form_value["item_name"]= input.getlist("item_name")
        form_value["item_description"]= input.getlist("item_description")
        form_value["item_quantity"]=input.getlist("item_quantity")
        form_value["donation_date"]=input.getlist("donation_date")
        form_value["comments"]=input.getlist("comments")

        for field,values in form_value.items():
            for  value in values:
                #todo add-2
                if not value and field == "donor_firstname":
                    flash("Donor First Name is required.", "danger")
                    has_error =True
                #todo add-3
                elif not value and field == "donor_lastname":
                    flash("Donor Last Name is required.","danger")
                    has_error =True
                #todo add-4
                elif not value and field == "donor_email" and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
                    flash("Invalid email format. Please enter a valid email address", "danger")
                    has_error = True
                #todo add-5
                elif not value and field == "organization_id":
                    flash("Organization ID is required.","danger")
                    has_error =True
                #todo add-6
                elif not value and field == "item_name":
                    flash("Item name is required.","danger")
                    has_error =True
                
                #todo add-8
                elif not value and field =="item_quantity":
                    flash("Item quantity is required.","danger")
                    has_error =True
                
                elif not value.isnumeric() or int(value) <=0:
                    flash("Item quantity must be a positive number.","danger")
                    has_error =True
                #todo add-9
                elif not value and field == "donation_date":
                    try:
                        donation_date = datetime.strptime(form_value["donation_date"], "%Y-%m-%d")
                        thirty_days_ago = datetime.now() - timedelta(days=30)
                        if donation_date < thirty_days_ago:
                            flash("Donation date must be within the past 30 days.", "danger")
                            has_error = True
                    except ValueError:
                        flash("Invalid date format. Please use YYYY-MM-DD.", "danger")
                        has_error = True

                   

       
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Donations (donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, donation_date)
                VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(organization_id)s, %(item_name)s, %(item_description)s, %(donation_date)s) """,form_value )# <-- TODO add-11 add query and add arguments
                if result.status:
                    print("donation record created")
                    flash("Created Donation Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash(f"Unexpected error while trying to search employee: {e}", "danger")
    return render_template("manage_donation.html",donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}
    
    # TODO edit-1 request args id is required (flash proper error message)
    input = request.form
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
       flash("Company ID is not available","Danger")
       redirect('/employee/search')
    else:
        if request.method == "POST":
            
            # TODO add-2 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            # TODO add-3 donor_firstname is required (flash proper error message)
            # TODO add-4 donor_lastname is required (flash proper error message)
            # TODO add-5 donor_email is required (flash proper error message)
            # TODO add-5a email must be in proper format (flash proper message)
            # TODO add-6 organization_id is required (flash proper error message)
            # TODO add-7 item_name is required (flash proper error message)
            # TODO add-8 item_description is optional
            # TODO add-9 item_quantity is required and must be more than 0 (flash proper error message)
            # TODO add-10 donation_date is required and must be within the past 30 days
            # TODO add-11 comments are optional
            #Zahooruddin zohaib moahmmed-zm254-11/20/23
            form_value={}
            has_error = False # use this to control whether or not an insert occurs
            form_value["donor_firstname"] = input.getlist("donor_firstname")
            form_value["donor_lastname"] = input.getlist("donor_lastname")
            form_value["donor_email"] = input.getlist("donor_email")
            form_value["organization_id"]= input.getlist("organization_id")
            form_value["item_name"]= input.getlist("item_name")
            form_value["item_description"]= input.getlist("item_description")
            form_value["item_quantity"]=input.getlist("item_quantity")
            form_value["donation_date"]=input.getlist("donation_date")
            form_value["comments"]=input.getlist("comments")

            for field,values in form_value.items():
                for  value in values:
                    #todo edit-2
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    if not value and field == "donor_firstname":
                        flash("Donor First Name is required.", "danger")
                        has_error =True
                    #todo edit-3
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    elif not value and field == "donor_lastname":
                        flash("Donor Last Name is required.","danger")
                        has_error =True
                    #todo edit-4
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    elif not value and field == "donor_email" and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
                        flash("Invalid email format. Please enter a valid email address", "danger")
                        has_error = True
                    #todo edit-5
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    elif not value and field == "organization_id":
                        flash("Organization ID is required.","danger")
                        has_error =True
                    #todo edit-6
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    elif not value and field == "item_name":
                        flash("Item name is required.","danger")
                        has_error =True
                    
                    #todo edit-8
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    elif not value and field =="item_quantity":
                        flash("Item quantity is required.","danger")
                        has_error =True
                    
                    elif not value.isnumeric() or int(value) <=0:
                        flash("Item quantity must be a positive number.","danger")
                        has_error =True
                    #todo edit-9
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    elif not value and field == "donation_date":
                        try:
                            donation_date = datetime.strptime(form_value["donation_date"], "%Y-%m-%d")
                            thirty_days_ago = datetime.now() - timedelta(days=30)
                            if donation_date < thirty_days_ago:
                                flash("Donation date must be within the past 30 days.", "danger")
                                has_error = True
                        except ValueError:
                            flash("Invalid date format. Please use YYYY-MM-DD.", "danger")
                            has_error = True

            if not has_error:
                try:
                    # TODO edit-12 fill in proper update query
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    result = DB.update("""
                    UPDATE IS601_MP3_Donations SET
                    donor_firstname = %(donor_firstname)s,
                    donor_lastname = %(donor_lastname)s,
                    donor_email = %(donor_email)s,
                    organization_id = %(organization_id)s,
                    item_name = %(item_name)s,
                    item_description = %(item_description)s,
                    donation_date = %(donation_date)s
                    WHERE id = %(donation_id)s
                    """, form_value)
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-13 make this user-friendly
                    #Zahooruddin zohaib moahmmed-zm254-11/20/23
                    print(f"update error {e}")
                    flash("Failed to update record. Please try again.", "danger")
        
        try:
            # TODO edit-14 fetch the updated data 
            #Zahooruddin zohaib moahmmed-zm254-11/20/23
            result = DB.selectOne("""SELECT d.id, d.donor_firstname, d.donor_lastname, d.donor_email, d.organization_id, 
                       d.item_name, d.item_description, d.item_quantity, d.donation_date, d.comments,o.organization_name
                        FROM IS601_MP3_Donations d
                        LEFT JOIN IS601_MP3_Organizations o ON d.organization_id = o.id
                        WHERE d.id = %(id)s""", {"id": id})
            
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-15 make this user-friendly
            #Zahooruddin zohaib moahmmed-zm254-11/20/23
            print(e)
            flash(f"Unexpected error while trying to fetch updated data: {e}", "danger")
    
    return render_template("manage_donation.html", donation=row)

@donations.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    id = request.args.get("id")
    if not id:
        flash("ID is missing. Please provide a valid ID.", "danger")
        return redirect(url_for("donations.search"))
    try:
        # TODO delete-2 delete donation by id (fetch the id from the request)
        result = DB.deleteOne("DELETE FROM IS601_MP3_Donations WHERE id = %(id)s", {"id": id})
        if result.status:  
            # TODO delete-3 ensure a flash message shows for successful delete
            flash("Successfully deleted the donation record.", "success")
        else:
            # TODO delete-4 pass all argument except id to this route
            flash("Failed to delete the donation record.", "danger")
            return redirect(url_for("donations.search", **request.args))
    except Exception as e:
        # TODO delete-5 redirect to donation search
        flash(f"Unexpected error while trying to delete the donation record: {e}", "danger")


    # return redirect(url_for("donations.search", **args))