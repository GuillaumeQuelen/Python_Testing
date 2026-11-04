import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime

MAX_PLACES_PER_COMPETITION = 12

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
bookings = {}


def is_past(competition):
    date = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
    return date < datetime.now()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def showSummary():
    matching = [club for club in clubs if club['email'] == request.form['email']]
    if not matching:
        flash("Sorry, this email is unknown.")
        return render_template('index.html')
    club = matching[0]
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if is_past(foundCompetition):
        flash("This competition is over: booking is closed.")
        return render_template('welcome.html', club=foundClub, competitions=competitions)
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    if is_past(competition):
        flash("This competition is over: booking is closed.")
        return render_template('welcome.html', club=club, competitions=competitions)
    placesRequired = int(request.form['places'])
    key = (competition['name'], club['name'])
    already_booked = bookings.get(key, 0)
    if placesRequired + already_booked > MAX_PLACES_PER_COMPETITION:
        flash("You cannot book more than 12 places per competition.")
        return render_template('welcome.html', club=club, competitions=competitions)
    if placesRequired > int(club['points']):
        flash("You do not have enough points.")
        return render_template('welcome.html', club=club, competitions=competitions)
    if placesRequired > int(competition['numberOfPlaces']):
        flash("Not enough places left in this competition.")
        return render_template('welcome.html', club=club, competitions=competitions)
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
    club['points'] = int(club['points']) - placesRequired
    bookings[key] = already_booked + placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/points')
def points():
    return render_template('points.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))