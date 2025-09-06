from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(_name_)

# --- Connexion à la base ---
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- Page d'accueil ---
@app.route('/')
def index():
    return "<h1>Bienvenue sur CodeStart </h1><p>Un projet pour apprendre à coder.</p>"

# --- Afficher tous les utilisateurs ---
@app.route('/users')
def users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return "<br>".join([f"{u['id']} - {u['name']}" for u in users])
# --- Ajouter un utilisateur ---
@app.route('/add/<name>')
def add_user(name):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return f" Utilisateur {name} ajouté avec succès !"

if _name_ == '_main_':
    app.run(debug=True)
