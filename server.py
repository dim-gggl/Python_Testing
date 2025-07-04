import json
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for
)

from config import SECRET_KEY
from manager import DataManager
from models import CompetitionPlace


app = Flask(__name__)
app.secret_key = SECRET_KEY

data_manager = DataManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_summary', methods=['POST'])
def show_summary():
    chosen_club = data_manager.find_club_by_email(request.form['email'])
    return render_template(
        'welcome.html',
        club=chosen_club,
        competitions=data_manager.competitions
    )

@app.route('/book/<competition>/<club>')
def book(competition, club):
    club = club.replace('_', ' ').title()
    competition = competition.replace('_', ' ').title()
    found_club = data_manager.find_club_by_name(club)
    found_competition = data_manager.find_competition_by_name(competition)
    if found_club and found_competition:
        return render_template(
            'booking.html',
            club=found_club,
            competition=found_competition
        )
    else:
        flash("Something went wrong-please try again")
        return render_template(
            'welcome.html',
            club=club,
            competitions=data_manager.competitions
        )

@app.route('/purchase_places', methods=['POST'])
def purchase_places():
    try:
        competition = data_manager.find_competition_by_name(request.form['competition'])
        club = data_manager.find_club_by_name(request.form['club'])
        places_required = int(request.form['places'])
        
        if places_required <= 0:
            flash('The number of places must be positive.')
            return render_template(
                'welcome.html',
                club=club,
                competitions=data_manager.competitions
            )
        
        if club.points < places_required:
            flash(
                f'Not enough points. The club has {club.points} points but '
                f'requests {places_required} places.'
            )
            return render_template(
                'welcome.html',
                club=club,
                competitions=data_manager.competitions
            )
        
        if competition.number_of_places < places_required:
            flash(
                f'Not enough places available. The competition has '
                f'{competition.number_of_places} places available but '
                f'{places_required} are requested.'
            )
            return render_template(
                'welcome.html',
                club=club,
                competitions=data_manager.competitions
            )
        
        current_places = club.get_places_for_competition(competition.name)
        if current_places + places_required > 12:
            flash(
                f'Cannot add {places_required} places. The club already has '
                f'{current_places} places for this competition. Maximum '
                'allowed: 12.'
            )
            return render_template(
                'welcome.html',
                club=club,
                competitions=data_manager.competitions
            )
        
        competition.number_of_places -= places_required
        club.points -= places_required
        competition_place = CompetitionPlace(competition)
        club.add_competition_place(competition_place, places_required)
        
        data_manager.save_data()
        flash('Reservation successful!')
        
    except (IndexError, ValueError) as e:
        flash(f'Error during reservation: {str(e)}')
    except Exception as e:
        flash(f'Unexpected error: {str(e)}')
    
    return render_template(
        'welcome.html',
        club=club,
        competitions=data_manager.competitions
    )

@app.route('/points_display')
def points_display():
    return render_template('display_points.html', clubs=data_manager.clubs)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)