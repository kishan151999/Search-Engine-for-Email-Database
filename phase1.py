import re

def get_next_email(file):
  email = file.readline()
  return email[6:len(email)-8]

def get_info(email, tag):
  start = "<" + tag + ">"
  end = "</" + tag + ">"
  return email[(email.index(start) + len(start)) : (email.index(end))]

def terms(row, subj, body, f):

  body = body.replace("&lt", "<").replace("&gt", ">").replace("&amp", "&").replace("&apos", "\'").replace("&quot", "\"")
  subj = subj.replace("&lt", "<").replace("&gt", ">").replace("&amp", "&").replace("&apos", "\'").replace("&quot", "\"")
  
  special_char_format = "&#[0-9]+"
  body = re.sub(special_char_format, " ", body)
  subj = re.sub(special_char_format, " ", subj)

  allowed_char = [x for x in "0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm-_"]
  final_body = (''.join([x if x in allowed_char else " " for x in body])).split()
  final_subj = (''.join([x if x in allowed_char else " " for x in subj])).split()

  for i in range(len(final_body)):
    if (len(final_body[i]) <= 2):
      final_body[i] = ""

  for i in range(len(final_subj)):
    if (len(final_subj[i]) <= 2):
      final_subj[i] = ""

  final_body = (' '.join(final_body)).split()
  final_subj = (' '.join(final_subj)).split()

  for text in final_subj:
    line = "s-" + text.lower() + ":" + str(row) + "\n"
    f.write(line)

  for text in final_body:
    line = "b-" + text.lower() + ":" + str(row) + "\n"
    f.write(line)

def emails(row, from_, to_, cc, bcc, f):
  if (from_ != ""):
    if ("," in from_):
      fr = from_.split(",")
      for i in fr:
        line = "from-" + i + ":" + str(row) + "\n"
        f.write(line)
    else:
      line = "from-" + from_ + ":" + str(row) + "\n"
      f.write(line)
  if (to_ != ""):
    if ("," in to_):
      t = to_.split(",")
      for i in t:
        line = "to-" + i + ":" + str(row) + "\n"
        f.write(line)
    else:
      line = "to-" + to_ + ":" + str(row) + "\n"
      f.write(line)
  if (cc != ""):
    if ("," in cc):
      c = cc.split(",")
      for i in c:
        line = "cc-" + i + ":" + str(row) + "\n"
        f.write(line)
    else:
      line = "cc-" + cc + ":" + str(row) + "\n"
      f.write(line)
  if (bcc != ""):
    if ("," in bcc):
      bc = bcc.split(",")
      for i in bc:
        line = "bcc-" + i + ":" + str(row) + "\n"
        f.write(line)
    else:
      line = "bcc-" + bcc + ":" + str(row) + "\n"
      f.write(line)

def dates(row, date, f):
  if (date != ""):
    line = date + ":" + str(row) + "\n"
    f.write(line)

def recs(row, email, f):
  line = str(row) + ":<mail>" + email + "</mail>\n"
  f.write(line)

def main():
  fileName = input("Please entered the xml filename: ")
  if (fileName == ""):
    fileName = "text2.xml"
  data = open(fileName, 'r')
  data.readline()
  data.readline()
  email = get_next_email(data)


  f_terms = open("terms.txt", "w")
  f_emails = open("emails.txt", "w")
  f_dates = open("dates.txt", "w")
  f_recs = open("recs.txt", "w")

  while (email != ""):
    #print("test")
    row = get_info(email,"row")
    date = get_info(email,"date")
    from_ = get_info(email,"from")
    to_ = get_info(email,"to")
    subj = get_info(email,"subj")
    cc = get_info(email,"cc")
    bcc = get_info(email,"bcc")
    body = get_info(email,"body")

    terms(row, subj, body, f_terms)
    emails(row, from_, to_, cc, bcc, f_emails)
    dates(row, date, f_dates)
    recs(row, email, f_recs)
    email = get_next_email(data)

  f_terms.close()
  f_emails.close()
  f_dates.close()
  f_recs.close()



if __name__ == "__main__":
  main()

