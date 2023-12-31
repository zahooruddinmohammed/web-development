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
    #zahooruddin zohaib moahmmed -zm254-18/11/23
    query = """ SELECT
            d.id,
            donor_firstname,
            donor_lastname,
            donor_email,
            organization_id,
            item_name,
            item_description,
            item_quantity,
            donation_date,
            comments,
            o.name as organization_name
        FROM IS601_MP3_Donations d
        LEFT JOIN IS601_MP3_Organizations o ON d.organization_id = o.id
        WHERE 1=1"""
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
    #zahooruddin zohaib moahmmed -zm254-18/11/23
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    donor_firstname = request.args.get("donor_firstname")
    donor_lastname = request.args.get("donor_lastname")
    donor_email = request.args.get("donor_email")
    item_name = request.args.get("item_name")
    organization_id = request.args.get("organization_id")
    column = request.args.get("column", )
    order = request.args.get("order", )
    limit = request.args.get("limit", )
    if donor_firstname:
        query += " AND donor_firstname LIKE %(donor_firstname)s"
        args["donor_firstname"] = f"%{'donor_firstname'}%"
    # TODO search-4 append like filter for donor_lastname if provided
    if donor_lastname:
        query += " AND donor_lastname LIKE %(donor_lastname)s"
        args["donor_lastname"] = f"%{'donor_lastname'}%"
    # TODO search-5 append like filter for donor_email if provided
    if donor_email:
        query += " AND donor_email LIKE %(donor_email)s"
        args["donor_email"] = f"%{'donor_email'}%"
    # TODO search-6 append like filter for item_name if provided
    if item_name:
        query += " AND item_name LIKE %(item_name)s"
        args["item_name"] = f"%{request.args.get('item_name')}%"
    if organization_id:
        query += " and d.organization_id=%(organization_id)s"
        args["organization_id"]= organization_id
    if column and order and column in allowed_columns  and order in ["asc","desc"]:
            if column == 'created':
                column = 'd.created'
            if column == 'modified':
                column = 'd.modified'
            if column == 'organization_name':
                  column = 'organization_name'
            query += f" ORDER BY {column} {order}"
    #zm254-10/18/23
    #zahooruddin zohaib moahmmed -zm254-18/11/23



    #limit = request.args.get("limit", 10)
    if limit:
        try:
            limit = int(limit)
            if 1 < limit <= 100:
                limit = limit
            else:
                limit = 10
                flash("Limit must be between 2 and 100", "error")
        except ValueError:
            limit = 10
            flash("Limit must be a valid number", "error")
    if not limit:
          limit =10
    
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    print("query",query)
    print("args", args)
    
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            #print(f"rows: {rows}")
    except Exception as e:
        # TODO search-11 make message user friendly
        #zahooruddin zohaib mohammed-11-18-23
        print(e)
        flash(f"Unexpected error while trying to search zz : {e}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    # TODO search-12 if request args has organization identifier set organization_name variable to the correct name
    allowed_columns_for_template = [(column, column.replace("_", " ").title()) for column in allowed_columns]
    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns)
@donations.route("/add", methods=["GET","POST"])
def add():
    input = request.form
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

        #zahooruddin zohaib moahmmed -zm254-18/11/23
        has_error = False # use this to control whether or not an insert occurs

        donor_firstname= input.get("donor_firstname")
        if not donor_firstname:
                    flash("Donor First Name is required.", "danger")
                    has_error =True
                
        donor_lastname = input.get("donor_lastname")
        if not donor_lastname:
                    flash("Donor Last Name is required.","danger")
                    has_error =True
        donor_email = input.get("donor_email")
        if not  donor_email and not re.match(r"[^@]+@[^@]+\.[^@]+", donor_email):
                    flash("Invalid email format. Please enter a valid email address", "danger")
                    has_error = True
        
        organization_id = input.get("organization_id")
        if not organization_id:
                    flash("Organization ID is required.","danger")
                    has_error =True
        item_name = input.get("item_name")
        if not item_name:
                    flash("Item name is required.","danger")
                    has_error =True
                
        item_description= input.get("item_description")
        item_quantity =input.get("item_quantity")
        if not item_quantity or int(item_quantity) <1:
                    flash("Item quantity is required and should be positive.","danger")
                    has_error =True
                
        donation_date =input.get("donation_date")
        if not donation_date:
                    try:
                        donation_date = datetime.strptime(donation_date, "%Y-%m-%d")
                        thirty_days_ago = datetime.now() - timedelta(days=30)
                        if donation_date < thirty_days_ago:
                            flash("Donation date must be within the past 30 days.", "danger")
                            has_error = True
                    except ValueError:
                        flash("Invalid date format. Please use YYYY-MM-DD.", "danger")
                        has_error = True

        comments =input.get("comments")

       
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Donations (donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments)
                VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(organization_id)s, %(item_name)s, %(item_description)s, %(item_quantity)s, %(donation_date)s, %(comments)s)
                """,{
                        'donor_firstname': donor_firstname,
                        'donor_lastname': donor_lastname,
                        'donor_email': donor_email,
                        'organization_id': organization_id,
                        'item_name': item_name,
                        'item_description': item_description,
                        'item_quantity': item_quantity,
                        'donation_date': donation_date,
                        'comments': comments
                    }
                )# <-- TODO add-11 add query and add arguments

                #zahooruddin zohaib moahmmed -zm254-18/11/23        
#                print("Query:", result.query)
 #               print("Arguments:", result.arguments)

                if result.status:
                    print("donation record created")
                    flash("Created Donation Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                #zahooruddin zohaib moahmmed -zm254-18/11/23
                flash(f"Unexpected error while trying to search add: {e}", "danger")
    return render_template("manage_donation.html",donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}

    #zahooruddin zohaib moahmmed -zm254-18/11/23
    # TODO edit-1 request args id is required (flash proper error message)
    input = request.form
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
       flash("Company ID is not available","Danger")
       return redirect(url_for('donations.search'))
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
            
            has_error = False # use this to control whether or not an insert occurs
            
            donor_firstname= input.get("donor_firstname")
            if not donor_firstname:
                        flash("Donor First Name is required.", "danger")
                        has_error =True
                    
            donor_lastname = input.get("donor_lastname")
            if not donor_lastname:
                        flash("Donor Last Name is required.","danger")
                        has_error =True
            donor_email = input.get("donor_email")
            if not  donor_email and not re.match(r"[^@]+@[^@]+\.[^@]+", donor_email):
                        flash("Invalid email format. Please enter a valid email address", "danger")
                        has_error = True
            
            organization_id = input.get("organization_id")
            if not organization_id:
                        flash("Organization ID is required.","danger")
                        has_error =True
            item_name = input.get("item_name")
            if not item_name:
                        flash("Item name is required.","danger")
                        has_error =True

            #zahooruddin zohaib moahmmed -zm254-18/11/23        
            item_description= input.get("item_description")

            item_quantity =input.get("item_quantity")
            if not item_quantity or int(item_quantity) <1:
                        flash("Item quantity is required and should be positive.","danger")
                        has_error =True
                    
            donation_date =input.get("donation_date")
            if not donation_date:
                        try:
                            donation_date = datetime.strptime(donation_date, "%Y-%m-%d")
                            thirty_days_ago = datetime.now() - timedelta(days=30)
                            if donation_date < thirty_days_ago:
                                flash("Donation date must be within the past 30 days.", "danger")
                                has_error = True
                        except ValueError:
                            flash("Invalid date format. Please use YYYY-MM-DD.", "danger")
                            has_error = True

            comments =input.get("comments")
                
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
                    item_quantity = %(item_quantity)s,
                    donation_date = %(donation_date)s,
                    comments = %(comments)s
                    WHERE id = %(donation_id)s
                    """, {'donor_firstname': donor_firstname,
                        'donor_lastname': donor_lastname,
                        'donor_email': donor_email,
                        'organization_id': organization_id,
                        'item_name': item_name,
                        'item_description': item_description,
                        'item_quantity': item_quantity,
                        'donation_date': donation_date,
                        'comments': comments,
                        'donation_id': id})
                    
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
            result = DB.selectOne("""SELECT d.id,
                                   donor_firstname,
                                   donor_lastname, 
                                  donor_email, 
                                  organization_id, 
                                    item_name,
                                   item_description,
                                   item_quantity, 
                                    donation_date,
                                    comments,
                                    o.name
                        FROM IS601_MP3_Donations d
                        LEFT JOIN IS601_MP3_Organizations o ON d.organization_id = o.id
                        WHERE d.id = %s""", id)
            
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
     # TODO delete-2 delete donation by id (fetch the id from the request)
      # TODO delete-3 ensure a flash message shows for successful delete
       # TODO delete-4 pass all argument except id to this route
       # TODO delete-5 redirect to donation search
    #zahooruddin zohaib mohammed-zm254-11/20/23
    id = request.args.get("id")
    args ={**request.args}
    if not id:
        flash("ID is missing. Please provide a valid ID.", "danger")
    if id:    
        try:
           
            #zahooruddin zohaib mohammed -zm254-11/20/23
            result = DB.delete("DELETE FROM IS601_MP3_Donations WHERE id = %s", id)
            if result.status:  
                flash("Successfully deleted the donation record.", "success")
          
        except Exception as e:
            print(e)
            flash(f"Unexpected error while trying to delete the donation record: {e}", "danger")
        del args["id"]
        
    return redirect(url_for("donations.search", **request.args))