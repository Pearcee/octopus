import os
import numpy as np
import fitz
from datetime import datetime, timedelta

dir = './PDF/'
files = os.listdir(dir)


def split_date(list):
    # print(list)
    day, month, year = list.split("\n")[1].split(" ")
    day = day.translate({ord(i): None for i in 'abcthstndr'})
    return datetime.strptime(day + month + year, "%d%B%Y")


def read_file(file):
    bigList = []
    doc = fitz.open(file)
    print(f"{file} number of pages: {doc.pageCount}")

    for pageNum in range(3,   doc.pageCount):  # 7
        page = doc.loadPage(pageNum)
        pagetext = page.getText("blocks")

        dates = pagetext[6][4]
        n = 14

        if "Incoming" in dates:
            dates = pagetext[7][4]
            n = 15
        day = split_date(dates)

        for text in range(n, len(pagetext)):
            # print(pagetext[text][4])
            time_from, col, time_to,  rate, consume, cost, nil = pagetext[text][4].replace("\n", " ").split(" ")
            h, m = time_from.split(":")
            time = day + timedelta(hours=int(h), minutes=int(m))
            bigList.append([time,  rate, consume, cost])

    return bigList


header = "day, rate, consume, cost"

for pdf in files:  
    file = dir + pdf
    list = read_file(file)
    file, tail = pdf.split(".")
    np.savetxt("./CSV/" + file + ".csv", list, comments='',
               delimiter=",", fmt='%s', header=header)
