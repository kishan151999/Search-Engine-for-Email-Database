import re
from bsddb3 import db
import os

def subj(key, prefix):
    Db_file = 'te.idx'
    database = db.DB()
    database.set_flags(db.DB_DUP)
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    once = True
    listi = []
    validprefix = False

    allkeys = []
    numletters = len(key) + 2

    if prefix == 1:
        for x in database.keys():
            x = str(x.decode("utf-8"))
            if x[0:numletters] == 's-' + key:
                allkeys.append(x)
                validprefix = True

    if validprefix == True:
        allkeys.append(key)
        for keyy in allkeys:
            once = True
            while (once):
                if keyy == key:
                    name = "s-" + keyy
                else:
                    name = keyy
                result = curs.set(name.encode("utf-8"))
                if result != None:
                    listi.append(str(result[1].decode("utf-8")))
                    dup = curs.next_dup()
                    while (dup != None):
                        listi.append(str(dup[1].decode("utf-8")))
                        dup = curs.next_dup()
                once = False

    elif validprefix == False:
        while (once):
            name = "s-" + key
            result = curs.set(name.encode("utf-8"))
            if result == None:
                curs.close()
                database.close()
                return None
            listi.append(str(result[1].decode("utf-8")))
            dup = curs.next_dup()
            while (dup != None):
                listi.append(str(dup[1].decode("utf-8")))
                dup = curs.next_dup()
            once = False

    listi = list(dict.fromkeys(listi))
    curs.close()
    database.close()
    return [int(x) for x in listi]



def body(key, prefix):
    Db_file = 'te.idx'
    database = db.DB()
    database.set_flags(db.DB_DUP)
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    once = True
    listi = []
    validprefix = False

    allkeys = []
    numletters = len(key) + 2

    if prefix == 1:
        for x in database.keys():
            x = str(x.decode("utf-8"))
            if x[0:numletters] == 'b-' + key:
                allkeys.append(x)
                validprefix = True

    if validprefix == True:
        allkeys.append(key)
        for keyy in allkeys:
            once = True
            while (once):
                if keyy == key:
                    name = "b-" + keyy
                else:
                    name = keyy
                result = curs.set(name.encode("utf-8"))
                if result != None:
                    listi.append(str(result[1].decode("utf-8")))
                    dup = curs.next_dup()
                    while (dup != None):
                        listi.append(str(dup[1].decode("utf-8")))
                        dup = curs.next_dup()
                once = False
    elif validprefix == False:
        while (once):
            name = "b-" + key
            result = curs.set(name.encode("utf-8"))
            if result == None:
                curs.close()
                database.close()
                return None
            listi.append(str(result[1].decode("utf-8")))
            dup = curs.next_dup()
            while (dup != None):
                listi.append(str(dup[1].decode("utf-8")))
                dup = curs.next_dup()
            once = False

    listi = list(dict.fromkeys(listi))
    curs.close()
    database.close()

    return [int(x) for x in listi]


def from_(key, prefix):
    Db_file = 'em.idx'
    database = db.DB()
    database.set_flags(db.DB_DUP)
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    once = True
    listi = []
    while (once):
        name = "from-" + key
        result = curs.set(name.encode("utf-8"))
        if result == None:
            curs.close()
            database.close()
            return None
        listi.append(str(result[1].decode("utf-8")))
        dup = curs.next_dup()
        while (dup != None):
            listi.append(str(dup[1].decode("utf-8")))
            dup = curs.next_dup()
        once = False
    listi = list(dict.fromkeys(listi))

    curs.close()
    database.close()

    return [int(x) for x in listi]


def to_(key, prefix):
    Db_file = 'em.idx'
    database = db.DB()
    database.set_flags(db.DB_DUP)
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)

    curs = database.cursor()
    once = True
    listi = []
    while (once):
        name = "to-" + key
        result = curs.set(name.encode("utf-8"))
        if result == None:
            curs.close()
            database.close()
            return None
        listi.append(str(result[1].decode("utf-8")))
        dup = curs.next_dup()
        while (dup != None):
            listi.append(str(dup[1].decode("utf-8")))
            dup = curs.next_dup()
        once = False
    listi = list(dict.fromkeys(listi))

    curs.close()
    database.close()

    return [int(x) for x in listi]


def cc(key, prefix):
    Db_file = 'em.idx'
    database = db.DB()
    database.set_flags(db.DB_DUP)
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    once = True
    listi = []
    while (once):
        name = "cc-" + key
        result = curs.set(name.encode("utf-8"))
        if result == None:
            curs.close()
            database.close()
            return None
        listi.append(str(result[1].decode("utf-8")))
        dup = curs.next_dup()
        while (dup != None):
            listi.append(str(dup[1].decode("utf-8")))
            dup = curs.next_dup()
        once = False
    listi = list(dict.fromkeys(listi))

    curs.close()
    database.close()

    return [int(x) for x in listi]


def bcc(key, prefix):
    Db_file = 'em.idx'
    database = db.DB()
    database.set_flags(db.DB_DUP)
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    once = True
    listi = []
    while (once):
        name = "bcc-" + key
        result = curs.set(name.encode("utf-8"))
        if result == None:
            curs.close()
            database.close()
            return None
        listi.append(str(result[1].decode("utf-8")))
        dup = curs.next_dup()
        while (dup != None):
            listi.append(str(dup[1].decode("utf-8")))
            dup = curs.next_dup()
        once = False
    listi = list(dict.fromkeys(listi))

    curs.close()
    database.close()

    return [int(x) for x in listi]


def date(key, prefix, operator):
    Db_file = 'da.idx'
    database = db.DB()
    database.set_flags(db.DB_DUP)
    database.open(Db_file, None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()
    validoperator = False
    allkeys = []
    once = True

    if operator == '<':
        for x in database.keys():
            x = str(x.decode("utf-8"))
            if x < key:
                allkeys.append(x)
                validoperator = True

    elif operator == '<=':
        for x in database.keys():
            x = str(x.decode("utf-8"))
            if x <= key:
                allkeys.append(x)
                validoperator = True

    elif operator == '>':
        for x in database.keys():
            x = str(x.decode("utf-8"))
            if x > key:
                allkeys.append(x)
                validoperator = True

    elif operator == '>=':
        for x in database.keys():
            x = str(x.decode("utf-8"))
            if x >= key:
                allkeys.append(x)
                validoperator = True

    listi = []
    if validoperator == True:
        if (operator == ">=" or operator == "<="):
            allkeys.append(key)
        for keyy in allkeys:
            once = True
            while (once):
                name = keyy
                result = curs.set(name.encode("utf-8"))
                if result != None:
                    listi.append(str(result[1].decode("utf-8")))
                    dup = curs.next_dup()
                    while (dup != None):
                        listi.append(str(dup[1].decode("utf-8")))
                        dup = curs.next_dup()
                once = False

    elif validoperator == False and operator == "=":
        while (once):
            name = key
            result = curs.set(name.encode("utf-8"))
            if result == None:
                curs.close()
                database.close()
                return None
            listi.append(str(result[1].decode("utf-8")))
            dup = curs.next_dup()
            while (dup != None):
                listi.append(str(dup[1].decode("utf-8")))
                dup = curs.next_dup()
            once = False

    listi = list(dict.fromkeys(listi))
    curs.close()
    database.close()

    return [int(x) for x in listi]

def all_row():
    database = db.DB()
    Db_file = 're.idx'
    database.open(Db_file, None, db.DB_HASH, db.DB_CREATE)
    allrows = []

    for x in database.keys():
        allrows.append(str(x.decode("utf-8")))

    database.close()
    return [int(x) for x in allrows]


def get_info(row):
    database = db.DB()
    Db_file = 're.idx'
    database.open(Db_file, None, db.DB_HASH, db.DB_CREATE)
    curs = database.cursor()
    listi = []
    name = row
    result = curs.set(name.encode("utf-8"))
    if result == None:
        curs.close()
        database.close()
        return None
    temp = (str(result[1].decode("utf-8")))
    curs.close()
    database.close()
    return temp


def full_subject(row):
    database = db.DB()
    Db_file = 're.idx'
    database.open(Db_file, None, db.DB_HASH, db.DB_CREATE)
    curs = database.cursor()
    listi = []
    name = row
    result = curs.set(name.encode("utf-8"))
    if result == None:
        curs.close()
        database.close()
        return None
    listi.append(str(result[1].decode("utf-8")))
    start = "<" + 'subj' + ">"
    end = "</" + 'subj' + ">"
    curs.close()
    database.close()
    return listi[0][(listi[0].index(start) + len(start)): (listi[0].index(end))]


def sub_body(key, prefix):
    s = subj(key, prefix)
    b = body(key, prefix)
    if (s == None):
        if (b == None):
            return None
        else:
            return [int(x) for x in b]
    else:
        if (b == None):
            return [int(x) for x in s]
        else:
            return [int(x) for x in (s+b)]


def split_input(user_input):
    subjPattern = "(subj([ ]*):([ ]*)([0-9a-zA-Z_-]+)([%]?)[ ]+)"
    bodyPattern = "(body([ ]*):([ ]*)([0-9a-zA-Z_-]+)([%]?)[ ]+)"
    fromPattern = "(from([ ]*):([ ]*)([0-9a-zA-Z_.@-]+)([%]?)[ ]+)"
    toPattern = "(to([ ]*):([ ]*)([0-9a-zA-Z_.@-]+)([%]?)[ ]+)"
    datePattern = "(date([ ]*)(:|<|<=|>|>=)([ ]*)([0-9]{4}/[0-9]{2}/[0-9]{2})([%]?)[ ]+)"
    ccPattern = "(cc([ ]*):([ ]*)([0-9a-zA-Z_.@-]+)([%]?)[ ]+)"
    bccPattern = "(bcc([ ]*):([ ]*)([0-9a-zA-Z_.@-]+)([%]?)[ ]+)"
    sub_bodyPattern = "(([0-9a-zA-Z_-]+)([%]?))"

    user_input = user_input.strip().lower() + " "

    sub_match = re.findall(subjPattern, user_input)
    body_match = re.findall(bodyPattern, user_input)
    from_match = re.findall(fromPattern, user_input)
    to_match = re.findall(toPattern, user_input)
    date_match = re.findall(datePattern, user_input)
    bcc_match = re.findall(bccPattern, user_input)

    result = all_row()

    if sub_match:
        for m in sub_match:
            user_input = user_input.replace(m[0], " ")
            selected = subj(m[3], [0, 1][m[4] == "%"])
            if (selected == None):
                return None
            result = [x for x in result if x in selected]

    user_input = user_input.strip() + " "

    if body_match:
        for m in body_match:
            user_input = user_input.replace(m[0], " ")
            selected = body(m[3], [0, 1][m[4] == "%"])
            if (selected == None):
                return None
            result = [x for x in result if x in selected]

    user_input = user_input.strip() + " "

    if from_match:
        for m in from_match:
            user_input = user_input.replace(m[0], " ")
            selected = from_(m[3], [0, 1][m[4] == "%"])
            if (selected == None):
                return None
            result = [x for x in result if x in selected]

    user_input = user_input.strip() + " "

    if to_match:
        for m in to_match:
            user_input = user_input.replace(m[0], " ")
            selected = to_(m[3], [0, 1][m[4] == "%"])
            if (selected == None):
                return None
            result = [x for x in result if x in selected]

    user_input = user_input.strip() + " "

    if bcc_match:
        for m in bcc_match:
            user_input = user_input.replace(m[0], " ")
            selected = bcc(m[3], [0, 1][m[4] == "%"])
            if (selected == None):
                return None
            result = [x for x in result if x in selected]

    user_input = user_input.strip() + " "

    cc_match = re.findall(ccPattern, user_input)

    if cc_match:
        for m in cc_match:
            user_input = user_input.replace(m[0], " ")
            selected = cc(m[3], [0, 1][m[4] == "%"])
            if (selected == None):
                return None
            result = [x for x in result if x in selected]

    user_input = user_input.strip() + " "

    if date_match:
        for m in date_match:
            user_input = user_input.replace(m[0], " ")
            selected = date(m[4], [0, 1][m[5] == "%"], [m[2], "="][m[2] == ":"])
            if (selected == None):
                return None
            result = [x for x in result if x in selected]

    user_input = user_input.strip() + " "

    sub_body_match = re.findall(sub_bodyPattern, user_input)

    if sub_body_match:
        for m in sub_body_match:
            user_input = user_input.replace(m[0], " ")
            selected = sub_body(m[1], [0, 1][m[2] == "%"])
            if (selected == None):
                return None
            result = [x for x in result if x in selected]

    user_input = user_input.strip()
    if (user_input.strip() != ""):
        print("Not formatted input")
        return None
    else:
        return result


def full_mode(user_input):
    result = split_input(user_input)
    if result:
      for r in result:
        print(str(r) + ": " + get_info(str(r).replace("&#10;", "")))
    else:
      print("None has selected")


def partial_mode(user_input):
    result = split_input(user_input)
    if result:
      for r in result:
        print(str(r) + ": " + full_subject(str(r).replace("&#10;", "")))
    else:
      print("None has selected")



def main():
  full = 0
  os.system('clear')
  while True:
    command = input("Input for command: (EXIT command: exit the 291 program)")
    command = command.lower() 

    if (command == "exit the 291 program"):
      print("Exit from the program")
      return 0

    if (command == "output=full"):
      full = 1
    if (command == "output=brief"):
      full = 0

    if (command != "output=brief" and command != "output=full"):
      if (full == 1):
        full_mode(command)
      else:
        partial_mode(command)
    t = input("Press enter to continue")
    os.system('clear')


if __name__ == "__main__":
    main()