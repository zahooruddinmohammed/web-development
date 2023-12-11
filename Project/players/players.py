from flask import Blueprint, flash, render_template, request, redirect, url_for,current_app 
from flask_login import current_user , login_required
from sql.db import DB  # Import your DB class
from utils.Cricbuzz import Cricbuzz
from utils.lazy import DictToObject
from players.forms import PlayerForm, PlayerSearchForm , PlayerFetchForm,AdminPlayerSearchForm , AssocForm
from roles.permissions import admin_permission 


#stocks = Blueprint('stocks', __name__, url_prefix='/stocks', template_folder='templates')
players = Blueprint('players', __name__, url_prefix='/players', template_folder='templates')

def get_total(partial_query, args={}):
    total = 0
    try:
        result = DB.selectOne("SELECT count(1) as total FROM "+partial_query, args)
        if result.status and result.row:
            total = int(result.row["total"])
    except Exception as e:
        print(f"Error getting total {e}")
        total = 0
    return total

                    
                
@players.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = PlayerFetchForm()  # Assuming you have a PlayerSearchForm for player search
    if form.validate_on_submit():
        try:
            from utils.Cricbuzz import Cricbuzz
            from utils.lazy import DictToObject
            player_data_list = Cricbuzz.get_player_stats(form.plrN.data)
            if player_data_list:
                for player_data in player_data_list:
                    player_result = DictToObject(player_data)

                result =  DB.insertOne(
                        """INSERT INTO IS601_Players (player_id, name, team_name, face_image_id, source)
                            VALUES (%s, %s, %s, %s, 'API')
                            ON DUPLICATE KEY UPDATE
                            name = VALUES(name),
                            team_name = VALUES(team_name),
                            face_image_id = VALUES(face_image_id),
                            source = VALUES(source)""",
                        player_result.id, player_result.name, player_result.teamName, player_result.faceImageId
                    )
                

                if result.status:
                        flash(f"Loaded player record for {player_result.name} from API", "success")
                else:
                        flash(f"Error loading player record from API: {result.error}", "danger")
            else:
                flash(f"No player found for {form.plrN.data}", "warning")

        except Exception as e:
            flash(f"Error loading player record: {e}", "danger")

    return render_template("player_Search.html", form=form)



@players.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = PlayerForm()

    if form.validate_on_submit():
        try:
            #zahooruddin zohaib mohammed - zm254-12/06/23
            result = DB.insertOne(
                """INSERT INTO IS601_Players (player_id, name, team_name, face_image_id, source)
                    VALUES (%s, %s, %s, %s, 'custom')
                    ON DUPLICATE KEY UPDATE
                    player_id = VALUES(player_id),
                    name = VALUES(name),   
                    team_name = VALUES(team_name),
                    face_image_id = VALUES(face_image_id),
                    source = VALUES(source)""",
                form.player_id.data, form.name.data, form.team_name.data, form.face_image_id.data
            )
            
            if result.status:
                flash(f"Created/updated player record for {form.name.data} (Custom Data)", "success")
        except Exception as e:
            flash(f"Error creating/updating player record: {e}", "danger")


    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Validation error in field '{field}': {error}", "danger")

    return render_template("player_form.html", form=form, type="Create")

@players.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    id = request.args.get("id")
    
    if id is None or not id.isdigit():
        flash("Invalid Player ID. Please provide a valid numeric ID.", "danger")
        return redirect(url_for("players.list"))
    
    try:
        result = DB.selectOne(
            "SELECT player_id, name, team_name, face_image_id, source FROM IS601_Players WHERE id = %s",
            id
        )
        
        if not result.status or not result.row:
            flash("Player record not found", "danger")
            return redirect(url_for("players.list"))
        
        form = PlayerForm(data=result.row)

        if form.validate_on_submit():
            try:
                # Additional Data Validation
                if not form.name.data.isalpha():
                    flash("Invalid player name. Please enter a valid name with alphabetic characters only.", "danger")
                    return render_template("player_form.html", form=form, type="Edit")

                # Update the existing player record in the database
                result = DB.insertOne(
                    "UPDATE IS601_Players SET name = %s, team_name = %s, face_image_id = %s, source = %s WHERE id = %s",
                    form.name.data, form.team_name.data, form.face_image_id.data, form.source.data, id
                )
                
                if result.status:
                    flash(f"Updated player record for {form.name.data}", "success")
                    return redirect(url_for("players.list"))
                else:
                    flash(f"Error updating player record: {result.error}", "danger")
            except Exception as e:
                flash(f"Error updating player record: {e}", "danger")
    except Exception as e:
        flash("Error fetching player record", "danger")
    
    return render_template("player_form.html", form=form, type="Edit")


@players.route("/list", methods=["GET"])
@admin_permission.require(http_exception=403)
def list():
    form = PlayerSearchForm(request.args)
    allowed_columns = ["player_id","name", "team_name", "face_image_id","source","created", "modified"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    
    query = """SELECT id, player_id, name, team_name, face_image_id, source,
    IFNULL((SELECT count(1) FROM IS601_fvrt WHERE user_id =%(user_id)s and player_fvrt_id= IS601_Players.id),0) as 'is_assoc'
    FROM IS601_Players
    WHERE 1=1"""
    args = {"user_id":current_user.id}
    where =""
    #zahooruddin zohaib mohammed- zm254 - 12/01/23
    # Filter logic from the search route

    if form.player_id.data:
        args["player_id"] =f"%{form.player_id.data}"
        where += " AND player_id LIKE %(player_id)s"
    if form.player_id.data:
        args["name"] =f"%{form.name.data}"
        where += " AND name LIKE %(name)s"
    if form.team_name.data:
        args["team_name"] =f"%{form.team_name.data}"
        where += " AND team_name LIKE %(team_name)s"
    if form.face_image_id.data:
        args["face_image_id"] =f"%{form.face_image_id.data}"
        where += " AND face_image_id LIKE %(face_image_id)s"
    
    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"
    #zahooruddin zohaib mohammed-zm254- 12/01/23
    
    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"

    
    result = DB.selectAll(query+where, args)
    rows = []

    if result.status and result.rows:
        rows = result.rows

    total_records = get_total(""" IS601_Players""")
    return render_template("player_list.html", rows=rows, form=form, total_records=total_records)

@players.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    args = {**request.args}
    
    if id:
        try:
            # Delete the player record from the database
            result = DB.delete("DELETE FROM IS601_Players WHERE id = %s", id)
            
            if result.status:
                flash("Deleted player record", "success")
            else:
                flash(f"Error deleting player record: {result.error}", "danger")
        except Exception as e:
            flash(f"Error deleting player record: {e}", "danger")
        
        del args["id"]
    else:
        flash("No ID present", "warning")
    
    return redirect(url_for("players.list", **args))


@players.route("/view", methods=["GET"])
def view():
    id = request.args.get("id")
    
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("players.list"))
    
    try:
        result = DB.selectOne(
            "SELECT id, player_id, name, team_name, face_image_id, source FROM IS601_Players WHERE id = %s",
            id
        )
        
        if result.status and result.row:
            return render_template("player_view.html", player=result.row)
        else:
            flash("Player record not found", "danger")
    except Exception as e:
        flash(f"Player error {e}", "danger")
    
    return redirect(url_for("players.list"))

@players.route("/track",methods=["GET"])
def track():
    id = request.args.get("id") 
    args = {**request.args}
    del args["id"]
    print(f"Received id: {id}")
    if not id:
        flash("Missing id parameter","danger")
    else:
        params = {"user_id": current_user.id, "player_fvrt_id": id}
        try:
            try:
                result = DB.insertOne("INSERT INTO IS601_fvrt(player_fvrt_id,user_id) VALUES(%(player_fvrt_id)s,%(user_id)s)  ", params)
                if result.status:
                    flash("Added player to your watch list","success")
            except Exception as e:
                print(f"Should just be a dub exception and can be ignored {e}")
                result = DB.delete("DELETE FROM IS601_fvrt WHERE player_fvrt_id =%(player_fvrt_id)s AND user_id=%(user_id)s",params)
                if result.status:
                    flash("Removed player form your fvrt list","success")
        except Exception as e:
            print(f"Error doing something with track/untrack{e}")
            flash("An unhandled error occured please try again","danger") 
    url = request.referrer
    if url:
        from urllib.parse import urlparse
        url_stuff = urlparse(url)
        watchlist_url = url_for("players.watchlist")
        print(f"Parsed url {url_stuff} {watchlist_url}")
        if url_stuff.path == url_for("players.watchlist"):
            return redirect(url_for("players.watchlist", **args))
        elif url_stuff.path == url_for("players.view"):
            args["id"] = id
            return redirect(url_for("players.view", **args))          
    
    return redirect(url_for("players.list"))

@players.route("/watchlist",methods =["GET"])
def watchlist():
    id = request.args.get("id", current_user.id)
    form = PlayerSearchForm(request.args)
    allowed_columns = ["player_id","name", "team_name", "face_image_id","source","created", "modified"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT t.id, player_id ,name, team_name, face_image_id, source, 
    IFNULL((SELECT count(1) FROM IS601_fvrt WHERE user_id = %(user_id)s and player_fvrt_id = t.id), 0) as 'is_assoc' 
    FROM IS601_Players t JOIN IS601_fvrt w ON t.id = w.player_fvrt_id
    WHERE w.user_id = %(user_id)s
    """
    args = {"user_id":id}
    where = ""

    if form.player_id.data:
        args["player_id"] =f"%{form.player_id.data}"
        where += " AND player_id LIKE %(player_id)s"
    if form.player_id.data:
        args["name"] =f"%{form.name.data}"
        where += " AND name LIKE %(name)s"
    if form.team_name.data:
        args["team_name"] =f"%{form.team_name.data}"
        where += " AND team_name LIKE %(team_name)s"
    if form.face_image_id.data:
        args["face_image_id"] =f"%{form.face_image_id.data}"
        where += " AND face_image_id LIKE %(face_image_id)s"

    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"

    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"
    
    result = DB.selectAll(query + where, args)
    rows = []

    if result.status and result.rows:
        rows = result.rows

    total_records = get_total(""" IS601_players t JOIN IS601_fvrt w ON t.id = w.player_fvrt_id
     WHERE w.user_id = %(user_id)s""", {"user_id": id})
    return render_template("player_list.html", rows=rows, form=form, title="Watchlist", total_records=total_records)

@players.route("/clear", methods=["GET"])
def clear():
    id = request.args.get("id")
    args = {**request.args}
    if "id" in args:
        del args["id"]
    if not id:
        flash("Missing id", "danger")
    else:
        if id == current_user.id or current_user.has_role("Admin"):
            try:
                result = DB.delete("DELETE FROM IS601_fvrt WHERE user_id = %(user_id)s", {"user_id":id})
                if result.status:
                    flash("Cleared watchlist", "success")
            except Exception as e:
                print(f"Error clearing watchlist {e}")
                flash("Error clearing watchlist","danger")
        

    return redirect(url_for("players.watchlist", **args))


@players.route("/associations", methods=["GET"])
@admin_permission.require(http_exception=403)
def associations():
    
    form = AdminPlayerSearchForm(request.args)
    allowed_columns = ["player_id","name", "team_name", "face_image_id","source","created", "modified"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT u.id as user_id, username, c.id, player_id,name, team_name, face_image_id, source
    FROM IS601_Players c JOIN IS601_WatchList w ON c.id = w.player_fvrt_id LEFT JOIN IS601_Users u on u.id = w.user_id
    WHERE 1=1
    """
    args = {}
    where = ""

    if form.player_id.data:
        args["player_id"] =f"%{form.player_id.data}"
        where += " AND player_id LIKE %(player_id)s"
    if form.player_id.data:
        args["name"] =f"%{form.name.data}"
        where += " AND name LIKE %(name)s"
    if form.team_name.data:
        args["team_name"] =f"%{form.team_name.data}"
        where += " AND team_name LIKE %(team_name)s"
    if form.face_image_id.data:
        args["face_image_id"] =f"%{form.face_image_id.data}"
        where += " AND face_image_id LIKE %(face_image_id)s"

    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"

    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"
    

    result = DB.selectAll(query + where, args)
    rows = []

    if result.status and result.rows:
        rows = result.rows

    total_records = get_total(""" IS601_Players t JOIN IS601_fvrt w ON t.id = w.player_fvrt_id
     WHERE w.user_id = %(user_id)s""", {"user_id": id})
    return render_template("player_list.html", rows=rows, form=form, title="Associations", total_records=total_records)

@players.route("/unwatched", methods=["GET"])
@login_required
def unwatched():
    form = PlayerSearchForm(request.args)
    allowed_columns = ["player_id","name", "team_name", "face_image_id","source","created", "modified"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT c.id,player_id, name, team_name ,face_image_id,
    IFNULL((SElECT count(1) FROM IS601_fvrt WHERE user_id = %(user_id)s and player_fvrt_id = c.id), 0) as 'is_assoc' 
    FROM IS601_Players c WHERE c.id not in (SELECT DISTINCT player_fvrt_id FROM IS601_fvrt)
    """
    args = {"user_id": current_user.id}
    where = ""
    if form.player_id.data:
        args["player_id"] =f"%{form.player_id.data}"
        where += " AND player_id LIKE %(player_id)s"
    if form.player_id.data:
        args["name"] =f"%{form.name.data}"
        where += " AND name LIKE %(name)s"
    if form.team_name.data:
        args["team_name"] =f"%{form.team_name.data}"
        where += " AND team_name LIKE %(team_name)s"
    if form.face_image_id.data:
        args["face_image_id"] =f"%{form.face_image_id.data}"
        where += " AND face_image_id LIKE %(face_image_id)s"

    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"
    
    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"
    
    result = DB.selectAll(query+where, args)
    rows = []
    
    if result.status and result.rows:
        rows = result.rows

    total_records = get_total(""" IS601_Players c 
     WHERE c.id not in (SELECT DISTINCT player_fvrt_id FROM IS601_fvrt)""")
    return render_template("player_list.html", rows=rows, form=form, title="Unwatched Items", total_records=total_records)

@players.route("/manage", methods=["GET"])
def manage():
    form = AssocForm(request.args)
    users = []
    players = []
    username = form.username.data
    player_name = form.player.data
    if username and player_name:
        result = DB.selectAll("SELECT id, username FROM IS601_Users WHERE username like %(username)s LIMIT 25",{"username":f"%{username}%"})
        if result.status and result.rows:
            users = result.rows
        result = DB.selectAll("SELECT id, name FROM IS601_Players WHERE name like %(player)s LIMIT 25", {"player":f"%{player_name}%"})
        if result.status and result.rows:
            players = result.rows
    print(f"Users {users}")
    print(f"Players {players}")
    return render_template("player_association.html", users=users, players=players, form=form)

@players.route("/manage_assoc", methods=["POST"])
def manage_assoc():
    users = request.form.getlist("users[]")
    players = request.form.getlist("players[]")
    print(users, players)
    args = {**request.args}
    if users and players: # we need both for this to work
        mappings = []
        for user in users:
            for player in players:
                mappings.append({"user_id":user, "player_fvrt_id":player})
        if len(mappings) > 0:
            for mapping in mappings:
                print(f"mapping {mapping}")
                try:
                    result = DB.insertOne("INSERT INTO IS601_fvrt (user_id, player_fvrt_id) VALUES(%(user_id)s, %(player_fvrt_id)s)", mapping)
                    if result.status:
                        pass
                        #flash(f"Successfully enabled/disabled roles for the user/role {len(mappings)} mappings", "success")
                except Exception as e:
                    print(f"Insert error {e}")
                    result = DB.delete("DELETE FROM IS601_fvrt WHERE user_id = %(user_id)s and player_fvrt_id = %(player_fvrt_id)s",mapping)
            flash("Successfully applied mappings", "success")
        else:
            flash("No user/card mappings", "danger")

    if "users" in args:
        del args["users"]
    if "cards" in args:
        del args["players"]
    return redirect(url_for("players.manage", **args))
