from bsddb3 import db
def main():
    recs()
    terms()
    emails()
    dates()

def recs():
    database = db.DB()
    Db_file = 're.idx'
    database.open(Db_file, None, db.DB_HASH, db.DB_CREATE)

    filetoread = open("recs.txt", 'r')

    for x in filetoread:
        x1, x2 = x.split(":", 1)
        x1 = x1.rstrip('\n')
        x2 = x2.rstrip('\n')
        x1 = str.encode(x1)
        database.put(x1, x2)

    database.close()
    filetoread.close()


def terms():
    database = db.DB()
    database.set_flags(db.DB_DUP)

    Db_file = 'te.idx'
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)

    filetoread = open("terms.txt", 'r')

    for x in filetoread:
        x1, x2 = x.split(":", 1)
        x1 = x1.rstrip('\n')
        x2 = x2.rstrip('\n')
        x1 = str.encode(x1)
        database.put(x1, x2)


    database.close()
    filetoread.close()

def emails():
    database = db.DB()
    database.set_flags(db.DB_DUP)
    Db_file = 'em.idx'
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)

    filetoread = open("emails.txt", 'r')

    for x in filetoread:
        x1, x2 = x.split(":", 1)
        x1 = x1.rstrip('\n')
        x2 = x2.rstrip('\n')
        x1 = str.encode(x1)
        database.put(x1, x2)

    database.close()
    filetoread.close()

def dates():
    database = db.DB()
    database.set_flags(db.DB_DUP)

    Db_file = 'da.idx'
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)

    filetoread = open("dates.txt", 'r')

    for x in filetoread:
        x1, x2 = x.split(":", 1)
        x1 = x1.rstrip('\n')
        x2 = x2.rstrip('\n')
        x1 = str.encode(x1)
        database.put(x1, x2)

    database.close()
    filetoread.close()


main()
