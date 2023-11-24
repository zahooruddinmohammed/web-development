from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB

import pycountry
organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, donation count as donations for the organization
    # don't do SELECT * and replace the below "..." portion
    #zahooruddin zohaib Mohammed-zm254-11/20/23
    allowed_columns = ["name", "city", "country", "state", "modified", "created"]
    query = """SELECT id, name, address, city, country, state, zip, website,
            (SELECT COUNT(*) FROM IS601_MP3_Donations WHERE organization_id = IS601_MP3_Organizations.id) as donations,
            created
            FROM IS601_MP3_Organizations WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
   
    
    # TODO search-2 get name, country, state, column, order, limit request args
    # TODO search-3 append a LIKE filter for name if provided
    # TODO search-4 append an equality filter for country if provided
    # TODO search-5 append an equality filter for state if provided
    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    filters = [("name", "name"), ("country", "country"), ("state", "state")]
    for filter_arg, filter in filters:
        if request.args.get(filter_arg):
            query += f" AND {filter} LIKE %s"
            args[f"%{request.args.get(filter_arg)}%"] = True

    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns and request.args.get("order") in ["asc", "desc"]:
            query += f" ORDER BY {request.args.get('column')} {request.args.get('order')}"
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
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        flash("An error occurred while fetching organizations. Please try again later.", "danger")

    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)


@organization.route("/add", methods=["GET","POST"])
def add():
    input = request.form
    if request.method == "POST":
        form_value ={}
        has_error = False # use this to control whether or not an insert occurs
        
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website, description
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation to solve this
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation to solve this
        # TODO add-7 website is not required
        # TODO add-8 zip is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # TODO add-9 description is not required
        #zahooruddin zohaib mohammed-zm254-11-20-23
        form_value["name"]= input.get('name')
        form_value["address"]=input.get('address')
        form_value["city"]=input.get('city')
        form_value["state"]=input.get('state')
        form_value["country"]=input.get('country')
        form_value["zip"]=input.get('zip')
        form_value["website"]=input.get('website')
        form_value["description"]=input.get('description')
        for field,values in form_value.items():
            for  value in values:
                #todo add-2
                 #zahooruddin zohaib mohammed-zm254-11-20-23
                if not value and field == "name":
                    flash("Name is required.", "danger")
                    has_error =True
                #todo add-3
                 #zahooruddin zohaib mohammed-zm254-11-20-23
                elif not value and field == "address":
                    flash("address is required.","danger")
                    has_error =True
                #todo add-4
                 #zahooruddin zohaib mohammed-zm254-11-20-23
                elif not value and field == "city":
                    flash("city is required.","danger")
                    has_error =True
                #todo add-5 & 5a
                 #zahooruddin zohaib mohammed-zm254-11-20-23
                elif  field == "state":
                    state= value
                    if not state:
                        flash("state is required.","danger")
                        has_error =True
                    else:
                        try:
                            state_obj = pycountry.subvisions.get(code=state)
                            if not state_obj:
                                flash("Invalid state code.","danger")
                                has_error =True
                        except Exception as e:
                            flash("An error occured while validating the state.","danger")
                            has_error =True
                #todo add-6 and 6a
                 #zahooruddin zohaib mohammed-zm254-11-20-23
                elif not value and field == "country":
                    flash("Country is required","danger")
                    has_error=True
                elif field =="country":
                    country  =value
                    if not country:
                        flash("Country is required","danger")
                    else:
                        try:
                            country_obj = pycountry.countries.get(alpha_2=country)
                            if not country_obj:
                                flash("Invalid country code.","danger")
                                has_error=True
                        except Exception as e:
                            flash("An error occured while validating the country.","Danger")
                            has_error =True
                #todo add-8\
                 #zahooruddin zohaib mohammed-zm254-11-20-23
                elif not value and field == "zip":
                    flash("Zip is required.","danger")
                    has_error=True
    
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Organizations (name, address, city, state, country, zip, website, description)
                VALUES
                (:name, :address, :city, :state, :country, :zip, :website , :description)
                """,  {
                    "name": request.form['name'],
                    "address": request.form['address'],
                    "city": request.form['city'],
                    "state": request.form['state'],
                    "country": request.form['country'],
                    "zip": request.form['zip'],
                    "website": request.form.get('website', ''),
                    "description": request.form.get('description', '')
                }) # <-- TODO add-10 add query and add arguments
                 #zahooruddin zohaib mohammed-zm254-11-20-23
                if result.status:
                    flash("Added Organization", "success")
            except Exception as e:
                # TODO add-11 make message user friendly
                flash("An error occurred while adding the organization. Please try again later.", "danger")
        
    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    #zahooruddin zohaib mohammed-zm254-11-20-23
    input = request.form
    id = request.args.get('id') 
    if not id: # TODO update this for TODO edit-1
        flash("organziation id is required.","danger")
     
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-3 name is required (flash proper error message)
            # TODO edit-4 address is required (flash proper error message)
            # TODO edit-5 city is required (flash proper error message)
            # TODO edit-6 state is required (flash proper error message)
            # TODO edit-6a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-7 country is required (flash proper error message)
            # TODO edit-7a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-8 website is not required
            # TODO edit-9 zipcode is required (flash proper error message)
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            has_error = False # use this to control whether or not an insert occurs
            form_value ={}
            #zahooruddin zohaib mohammed-zm254-11-20-23
            form_value["name"] = input.get('name')
            form_value["address"] = input.get('address')
            form_value["city"] = input.get('city')
            form_value["state"] = input.get('state')
            form_value["country"] = input.get('country')
            form_value["zip"] = input.get('zip')
            form_value["website"] = input.get('website')

            for field,values in form_value.items():
                for value in values:
                    #todo edit -3
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    if not value and field =="name":
                        flash("Name is requied.","danger")
                        has_error=True
                     #todo edit -4
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    elif not value and field =="address":
                        flash("address is required","danger")
                        has_error=True
                     #todo edit -5
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    elif not value and field =="city":
                        flash("city is required","danger")
                        has_error=True
                     #todo edit -6
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    elif not value and field =="state":
                        flash("state is required","danger")
                        has_error=True
                     #todo edit -6a
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    elif field == "state":
                        state = value
                        if not state:
                            flash("State is required.", "danger")
                            has_error = True
                        else:
                            try:
                                state_obj = pycountry.subdivisions.get(code=state)
                                if not state_obj:
                                    flash("Invalid state code.", "danger")
                                    has_error = True
                            except Exception as e:
                                flash("An error occurred while validating the state.", "danger")
                                has_error = True
                     #todo edit -7
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    elif not value and field == "country":
                        flash("Country is required.", "danger")
                        has_error = True
                     #todo edit -7a 
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    elif field == "country":
                        country = value
                        if not country:
                            flash("Country is required.", "danger")
                            has_error = True
                        else:
                            try:
                                country_obj = pycountry.countries.get(alpha_2=country)
                                if not country_obj:
                                    flash("Invalid country code.", "danger")
                                    has_error = True
                            except Exception as e:
                                flash("An error occurred while validating the country.", "danger")
                                has_error = True
                    #todo edit -9 
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    elif not value and field == "zip":
                        flash("zip is required.","danger")
                        has_error=True
           
            if not has_error:
                try:
                    # TODO edit-10 fill in proper update query
                    # name, address, city, state, country, zip, website
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    result = DB.update("""
                        UPDATE IS601_MP3_Organizations
                        SET name = %(name)s, address = %(address)s, city = %(city)s, state = %(state)s,
                        country = %(country)s, zip = %(zip)s, website = %(website)s
                        WHERE id = %(id)s
                        """, {
                                "id": id,
                                "name": request.form['name'],
                                "address": request.form['address'],
                                "city": request.form['city'],
                                "state": request.form['state'],
                                "country": request.form['country'],
                                "zip": request.form['zip'],
                                "website": request.form.get('website', ''),})
                                                
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-11 make this user-friendly
                    #zahooruddin zohaib mohammed-zm254-11-20-23
                    print(f"{e}")
                    flash("An error occurred while updating the organization. Please try again later.", "danger")
        row = {}
        try:
            # TODO edit-12 fetch the updated data
            #zahooruddin zohaib mohammed-zm254-11-20-23
            result = DB.selectOne("SELECT * FROM IS601_MP3_Organizations WHERE id = %(id)s", {"id": id})
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-13 make this user-friendly
            #zahooruddin zohaib mohammed-zm254-11-20-23
            flash("An error occurred while fetching organization details. Please try again later.", "danger")
    
    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
     #zahooruddin zohaib mohammed-zm254-11-20-23
    id = request.args.get('id')
    if not id:
        flash("organziation id is reuqired.","danger")
        return redirect(url_for("organization.search"))
    try:
    # TODO delete-2 delete organization by id (note: you'll likely need to trigger a delete of all donations related to this organization first due to foreign key constraints)
     #zahooruddin zohaib mohammed-zm254-11-20-23
     
        result = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id = %s", id)

        if result.status:
            flash("Organization deleted successfully.","success")
        else:
            flash("Failed to delete organization.Please try again later.","danger")
    except Exception as e:
    # TODO delete-3 ensure a flash message shows for successful delete
     #zahooruddin zohaib mohammed-zm254-11-20-23
        flash("An error occured while deleting the organization.try again later.","danger")
    # TODO delete-4 pass all argument except id to this route
     #zahooruddin zohaib mohammed-zm254-11-20-23
    args = request.args.copy()
    args.pop('id',None)
    # TODO delete-5 redirect to organization search
    return redirect(url_for("organization.search",**args))


    # return redirect(url_for("organization.search", **args))