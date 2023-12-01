from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
#from stocks.forms import StockForm, StockSearchForm  # Import your StockForm class
#from utils.Cricbuzz import Cricbuzz
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
            # Create a new stock record in the database
            result = Cricbuzz.get_player_stats(form.name.data)
            if result:
                result = DictToObject(result)
                #result.change_percent = result.change_percent.replace("%","")
                result = DB.insertOne(
                    """INSERT INTO IS601_Players (player_id, name, team_name, face_image_id)
                        VALUES (%s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        name = VALUES(name),
                        team_name = VALUES(team_name),
                        face_image_id = VALUES(face_image_id)""",
                    result.id, result.name, result.teamName, result.faceImageId
                )
                if result.status:
                    flash(f"Loaded player record for {form.name.data}", "success")
        except Exception as e:
            flash(f"Error loading player record: {e}", "danger")
    return render_template("player_search.html", form=form)

@players.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = PlayerForm()
    if form.validate_on_submit():
        try:
            # Create a new stock record in the database
            result = DB.insertOne(
                "INSERT INTO IS601_PLayers (player_id, name, team_name, face_image_id) VALUES (%s, %s, %s, %s))",
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
    form = playerForm()
    player_id = request.args.get("player_id")
    if player_id is None:
        flash("Missing Player ID", "danger")
        return redirect(url_for("players.list"))
    if form.validate_on_submit() and player_id:
        try:
            # Update the existing stock record in the database
            result = DB.insertOne(
                "UPDATE IS601_players SET name = %s, team_name = %s, face_image_id = %s WHERE player_id = %s",
                form.name.data, form.team_name.data, form.face_image_id.data, player_id
            )
            if result.status:
                flash(f"Updated player record for {form.name.data}", "success")
        except Exception as e:
            flash(f"Error updating player record: {e}", "danger")
    try:
        result = DB.selectOne(
            "SELECT player_id, name, team_name, face_image_id FROM IS601_players WHERE player_id = %s",
            player_id
        )
        if result.status and result.row:
            form = PlayerForm(data=result.row)
    except Exception as e:
        flash("Error fetching player record", "danger")
    return render_template("player_form.html", form=form, type="Edit")

@stocks.route("/list", methods=["GET"])
@admin_permission.require(http_exception=403)
def list():
    rows = []
    try:
        result = DB.selectAll("SELECT player_id, name, team_name, face_image_id FROM IS601_Players LIMIT 100")
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)
        flash("Error getting player records", "danger")
    return render_template("players_list.html", rows=rows)

@players.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    player_id = request.args.get("player_id")
    args = {**request.args}
    if player_id:
        try:
            # Delete the stock record from the database
            result = DB.delete("DELETE FROM IS601_Players WHERE player_id = %s", player_id)
            if result.status:
                flash("Deleted player record", "success")
        except Exception as e:
            flash(f"Error deleting player record: {e}", "danger")
        del args["player_id"]
    else:
        flash("No ID present", "warning")
    return redirect(url_for("players.list", **args))

@players.route("/view", methods=["GET"])
def view():
    player_id = request.args.get("player_id")
    if player_id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("playerss.list"))
    try:
        result = DB.selectOne(
            "SELECT player_id, name, team_name, face_image_id FROM IS601_Players WHERE player_id = %s",
            player_id
        )
        if result.status and result.row:
            return render_template("player_view.html", player=result.row)
        else:
            flash("player record not found", "danger")
    except Exception as e:
        print(f"player error {e}")
        flash("Error fetching player record", "danger")
    return redirect(url_for("players.list"))