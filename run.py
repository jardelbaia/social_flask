from social_flask import app, models, db, routes


def create_db():
    db.init_app(app)
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
