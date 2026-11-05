import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime
import os

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
app.secret_key = os.environ.get('SECRET_KEY', 'dev-only-key')


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
    foundClubs = [c for c in clubs if c['name'] == club]
    foundCompetitions = [c for c in competitions if c['name'] == competition]
    if not foundClubs or not foundCompetitions:
        flash("Something went wrong-please try again")
        return render_template('index.html')
    foundClub = foundClubs[0]
    foundCompetition = foundCompetitions[0]
    if is_past(foundCompetition):
        flash("This competition is over: booking is closed.")
        return render_template('welcome.html', club=foundClub, competitions=competitions)
    return render_template('booking.html', club=foundClub, competition=foundCompetition)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    foundCompetitions = [c for c in competitions if c['name'] == request.form['competition']]
    foundClubs = [c for c in clubs if c['name'] == request.form['club']]
    if not foundCompetitions or not foundClubs:
        flash("Something went wrong-please try again")
        return render_template('index.html')
    competition = foundCompetitions[0]
    club = foundClubs[0]
    if is_past(competition):
        flash("This competition is over: booking is closed.")
        return render_template('welcome.html', club=club, competitions=competitions)
    try:
        placesRequired = int(request.form['places'])
    except ValueError:
        placesRequired = 0
    if placesRequired <= 0:
        flash("Please enter a valid number of places.")
        return render_template('welcome.html', club=club, competitions=competitions)
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
