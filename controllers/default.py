start = 1
end = 20
EASY = 10
MODERATE = 20
DIFFICULT = 30

from random import randint
################################
def insert_easy():
    form = SQLFORM(db.easy_words).process()
    return locals()

def insert_moderate():
    form = SQLFORM(db.moderate_words).process()
    return locals()

def insert_difficult():
    form = SQLFORM(db.difficult_words).process()
    return locals()

def list_easy_words():
    rows = db(db.easy_words).select()
    return locals()

def list_moderate_words():
    rows = db(db.moderate_words).select()
    return locals()

def list_difficult_words():
    rows = db(db.difficult_words).select()
    return locals()

##################################################################
#TEST
def load_ques():
    FLAG = session.FLAG
    if session.ques_count == end:
        redirect(URL('end_test'))
    if session.FLAG == EASY:
        for i in range(1,len(db(db.easy_words).select())):
            ques_index = randint(1,len(db(db.easy_words).select()))
            if (ques_index, session.FLAG) not in session.count:
                ques = db.easy_words(ques_index)
                session.count.append((ques_index, session.FLAG))
                session.ind = ques_index
                session.ques_count = session.ques_count + 1
                length = len(db.easy_words(ques_index).word)
                break
    elif session.FLAG == MODERATE:
        for i in range(1,len(db(db.moderate_words).select())):
            ques_index = randint(1,len(db(db.moderate_words).select()))
            if (ques_index, session.FLAG) not in session.count:
                ques = db.moderate_words(ques_index)
                session.count.append((ques_index, session.FLAG))
                session.ind = ques_index
                session.ques_count = session.ques_count + 1
                length = len(db.moderate_words(ques_index).word)
                break
    elif session.FLAG == DIFFICULT:
         for i in range(1,len(db(db.difficult_words).select())):
            ques_index = randint(1,len(db(db.difficult_words).select()))
            if (ques_index, session.FLAG) not in session.count:
                ques = db.easy_words(ques_index)
                session.count.append((ques_index, session.FLAG))
                session.ind = ques_index
                session.ques_count = session.ques_count + 1
                length = len(db.difficult_words(ques_index).word)
                break
    return locals()

def check_ans():
    users_ans = request.vars.useranswer
    index_dd = session.ind
    
    if session.FLAG == EASY:
        answer = db.easy_words(index_dd).word
        if db.easy_words(index_dd).word.lower() == users_ans.lower():
            session.score = session.score + EASY
            session.track.append((session.FLAG, index_dd, 1))
            print "Correct!"
        else:
            session.score = session.score - EASY
            session.track.append((session.FLAG, index_dd, 0))
            print "Wrong! ANS is " + db.easy_words(index_dd).word
    elif session.FLAG == MODERATE:
        if db.moderate_words(index_dd).word.lower() == users_ans.lower():
            session.score = session.score + MODERATE
            session.track.append((session.FLAG, index_dd, 1))
        else:
            session.score = session.score - MODERATE
            session.track.append((session.FLAG, index_dd, 0))
    elif session.FLAG == DIFFICULT:
        if db.difficult_words(index_dd).word.lower() == users_ans.lower():
            session.score = session.score + DIFFICULT
            session.track.append((session.FLAG, index_dd, 1))
        else:
            session.score = session.score - DIFFICULT
            session.track.append((session.FLAG, index_dd, 0))
    sc = session.score
    redirect(URL('brains'))
    return locals()

def brains():
    if session.score < 50:
        session.FLAG = EASY
        print "In Easy"
    elif session.score >= 50 and session.score < 210:
        session.FLAG = MODERATE
        print "In Moderate"
    elif session.score >= 210 and session.score >= 480:
        session.FLAG = DIFFICULT
        print "In Difficult"
    redirect(URL('load_ques'))
    return locals()

def start_test():
    session.ind = start
    session.score = 0
    session.FLAG = EASY
    session.count = []
    session.ques_count = 0
    session.track = []
    return locals()

def show_ans():
    track = session.track
    rows = []
    for t in track:
        if t[0] == EASY:
            row = db.easy_words(t[1])
            if t[2] == 1:
                rows.append((row, 1))
            else:
                rows.append((row, 0))
        elif t[0] == MODERATE:
            row = db.moderate_words(t[1])
            if t[2] == 1:
                rows.append((row, 1))
            else:
                rows.append((row, 0))
        elif t[0] == DIFFICULT:
            row = db.difficult_words(t[1])
            if t[2] == 1:
                rows.append((row, 1))
            else:
                rows.append((row, 0))

    return locals()

def end_test():
    sc = session.score
    return locals()
#################################################################################
#POST

def display_your_form():
    form = SQLFORM(db.Suggestions)
    if form.process().accepted:
        redirect(URL('list_posts'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form = form)

def show():
        return dict(rows = db(db.Suggestions).select())
    
def list_posts():
    rows = db(db.Suggestions).select()
    return locals()
    
#################################################################################
def deck_page():
    session.ind = start
    session.score = 0
    session.FLAG = EASY
    session.count = []
    session.ques_count = 0
    session.track = []
    return locals()

def easy_deck():
    session.FLAG = EASY
    if session.ques_count == end:
        redirect(URL('end_test'))
 
    for i in range(1,len(db(db.easy_words).select())):
        ques_index = randint(1,len(db(db.easy_words).select()))
        if (ques_index, session.FLAG) not in session.count:
            ques = db.easy_words(ques_index)
            session.count.append((ques_index, session.FLAG))
            session.ind = ques_index
            session.ques_count = session.ques_count + 1
            length = len(db.easy_words(ques_index).word)
            break
    return locals()

def moderate_deck():
    session.FLAG = MODERATE
    for i in range(1,len(db(db.moderate_words).select())):
        ques_index = randint(1,len(db(db.moderate_words).select()))
        if (ques_index, session.FLAG) not in session.count:
            ques = db.moderate_words(ques_index)
            session.count.append((ques_index, session.FLAG))
            session.ind = ques_index
            session.ques_count = session.ques_count + 1
            length = len(db.moderate_words(ques_index).word)
            break
    return locals()

def difficult_deck():
    session.FLAG = DIFFICULT
    for i in range(1,len(db(db.difficult_words).select())):
        ques_index = randint(1,len(db(db.difficult_words).select()))
        if (ques_index, session.FLAG) not in session.count:
            ques = db.difficult_words(ques_index)
            session.count.append((ques_index, session.FLAG))
            session.ind = ques_index
            session.ques_count = session.ques_count + 1
            length = len(db.difficult_words(ques_index).word)
            break
    return locals()

def check_deck():
    users_ans = request.vars.useranswer
    index_dd = session.ind
    
    if session.FLAG == EASY:
        answer = db.easy_words(index_dd).word
        if db.easy_words(index_dd).word.lower() == users_ans.lower():
            session.score = session.score + EASY
            session.track.append((session.FLAG, index_dd, 1))
            print "Correct!"
        else:
            session.score = session.score - EASY
            session.track.append((session.FLAG, index_dd, 0))
            print "Wrong! ANS is " + db.easy_words(index_dd).word
        redirect('easy_deck')
    elif session.FLAG == MODERATE:
        if db.moderate_words(index_dd).word.lower() == users_ans.lower():
            session.score = session.score + MODERATE
            session.track.append((session.FLAG, index_dd, 1))
        else:
            session.score = session.score - MODERATE
            session.track.append((session.FLAG, index_dd, 0))
        redirect('moderate_deck')

    elif session.FLAG == DIFFICULT:
        if db.difficult_words(index_dd).word.lower() == users_ans.lower():
            session.score = session.score + DIFFICULT
            session.track.append((session.FLAG, index_dd, 1))
        else:
            session.score = session.score - DIFFICULT
            session.track.append((session.FLAG, index_dd, 0))
    redirect('difficult_deck')

    sc = session.score
    return locals()
#################################################################################
def index():

    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

def sample():
    return locals()

def word_listings():
    return locals()

def about_us():
    return locals()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
