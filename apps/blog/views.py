# coding: utf-8
from flask import request, session, g, redirect, url_for, render_template, flash
from models import app, db, Entries


@app.route('/')
def show_entries():
    cur = Entries.query.all()
    entries = [dict(id=row.id, title=row.title, text=row.text) for row in cur]
    return render_template('blog/show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    content = Entries(request.form['title'], request.form['text'])
    db.session.add(content)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/delete', methods=['POST', 'GET'])
def delete_entry():
    contents = Entries.query.all()
    for content in contents:
        db.session.delete(content)
        db.session.commit()
        return 'deleted:%d:%s_%s' % (content.id, content.title, content.text)
    return 'not data delete'


@app.route('/merge', methods=['POST', 'GET'])
def merge_entry():
    content = Entries.query.filter(Entries.id == 12).first()
    if content:
        content.title = content.title + u'谢谢'
        db.session.merge(content)
        db.session.commit()
        return 'merge:%d:%s_%s' % (content.id, content.title, content.text)
    return 'not data merge'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return 'You were logged in'
    return render_template('blog/login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run(debug=True)
