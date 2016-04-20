# -*- coding: utf-8 -*-
db.define_table("easy_words", Field("word", "string", requires = IS_NOT_EMPTY()), Field("meaning", "text", requires=IS_NOT_EMPTY()))
db.define_table("moderate_words", Field("word", "string", requires = IS_NOT_EMPTY()), Field("meaning", "text", requires=IS_NOT_EMPTY()))
db.define_table("difficult_words", Field("word", "string", requires = IS_NOT_EMPTY()), Field("meaning", "text", requires=IS_NOT_EMPTY()))

db.define_table("Suggestions",
    Field('Subject',requires=IS_NOT_EMPTY()),
    Field('Description','text',requires=IS_NOT_EMPTY()),
    Field('Author',requires=IS_NOT_EMPTY()))

#db.define_table("deck_words", Field("word", requires=IS_NOT_EMPTY()), Field("meaning", IS_NOT_EMPTY()), Field("deck", requires = IS_NOT_EMPTY()))
