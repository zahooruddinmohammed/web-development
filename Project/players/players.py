from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
#from stocks.forms import StockForm, StockSearchForm  # Import your StockForm class
#from utils.Cricbuzz import Cricbuzz
from players.forms import PlayerForm, PlayerSearchForm
from roles.permissions import admin_permission

#stocks = Blueprint('stocks', __name__, url_prefix='/stocks', template_folder='templates')
players = Blueprint('players', __name__, url_prefix='/players', template_folder='templates')

@players.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = PlayerSearchForm()
    if form.validate_on_submit():
        try:
            from utils.Cricbuzz import Cricbuzz
            from utils.lazy import DictToObject

            # Get the list of player records
            player_data_list = Cricbuzz.get_player_stats(form.plrN.data)
            
            if player_data_list:
                for player_data in player_data_list:
                    # Convert each player record to a DictToObject
                    player_result = DictToObject(player_data)
                    
                    # Insert or update the player record in the database
                    player_result = DB.insertOne(
                        """INSERT INTO IS601_Players (player_id, name, team_name, face_image_id)
                            VALUES (%s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE
                            name = VALUES(name),
                            team_name = VALUES(team_name),
                            face_image_id = VALUES(face_image_id)""",
                        player_result.id, player_result.name, player_result.teamName, player_result.faceImageId
                    )
                
                if player_result.status:
                    flash(f"Loaded player records for {form.plrN.data}", "success")
        except Exception as e:
            flash(f"Error loading player records: {e}", "danger")
    
            
    return render_template("player_search.html", form=form)

@players.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = PlayerForm()
    if form.validate_on_submit():
        try:
            # Create a new stock record in the database
            result = DB.insertOne(
                "INSERT INTO IS601_Players (player_id, name, team_name, face_image_id) VALUES (%s, %s, %s, %s)",
                form.player_id.data, form.name.data, form.team_name.data, form.face_image_id.data
            )
            if result.status:
                flash(f"Created player record for {form.name.data}", "success")
        except Exception as e:
            flash(f"Error creating player record: {e}", "danger")
    return render_template("player_form.html", form=form, type="Create")

@players.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    form = PlayerForm()
    id = request.args.get("id")
    
    if id is None:
        flash("Missing Player ID", "danger")
        return redirect(url_for("players.list"))
    
    if form.validate_on_submit() and id:
        try:
            # Update the existing player record in the database
            result = DB.insertOne(
                "UPDATE IS601_Players SET name = %s, team_name = %s, face_image_id = %s WHERE id = %s",
                form.name.data, form.team_name.data, form.face_image_id.data, id
            )
            
            if result.status:
                flash(f"Updated player record for {form.name.data}", "success")
            else:
                flash(f"Error updating player record: {result.error}", "danger")
        except Exception as e:
            flash(f"Error updating player record: {e}", "danger")
    
    try:
        result = DB.selectOne(
            "SELECT player_id, name, team_name, face_image_id FROM IS601_Players WHERE id = %s",
            id
        )
        
        if result.status and result.row:
            form = PlayerForm(data=result.row)
    except Exception as e:
        flash("Error fetching player record", "danger")
    
    return render_template("player_form.html", form=form, type="Edit")
@players.route("/list", methods=["GET"])
@admin_permission.require(http_exception=403)
def list():
    rows = []
    query = """SELECT id, player_id, name, team_name, face_image_id FROM IS601_Players WHERE 1=1"""
    args = {}
    allowed_columns = ["player_id", "name", "team_name", "face_image_id", "created", "modified"]

    # Filter logic from the search route
    player_id = request.args.get("player_id")
    name = request.args.get("name")
    team_name = request.args.get("team_name")
    column = request.args.get("column", )
    order = request.args.get("order", )
    limit = request.args.get("limit", )
    if player_id:
        query += " AND player_id LIKE %(player_id)s"
        args["player_id"] = f"%{player_id}%"

    if name:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{name}%"

    if team_name:
        query += " AND team_name LIKE %(team_name)s"
        args["team_name"] = f"%{team_name}%"

    if column and order and column in allowed_columns and order in ["asc", "desc"]:
        if column == 'created':
            column = 'created'
        if column == 'modified':
            column = 'modified'
        query += f" ORDER BY {column} {order}"

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
        limit = 10

    query += " LIMIT %(limit)s"
    args["limit"] = limit

    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        print(e)
        flash(f"Unexpected error while trying to fetch player records: {e}", "danger")

    return render_template("player_list.html", rows=rows, allowed_columns=allowed_columns)

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
            "SELECT id, player_id, name, team_name, face_image_id FROM IS601_Players WHERE id = %s",
            id
        )
        
        if result.status and result.row:
            return render_template("player_view.html", player=result.row)
        else:
            flash("Player record not found", "danger")
    except Exception as e:
        flash(f"Player error {e}", "danger")
    
    return redirect(url_for("players.list"))