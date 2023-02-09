import csv

def read_file_words(filename):
    s = open(f"lesson8_hw/random/{filename}.txt", "r",encoding='utf-8')
    out=s.read().split(',')
    s.close()
    return out

def read_csv(filename):
    csv = open(f"lesson8_hw/{filename}.csv", "r",encoding='utf-8')
    out=csv.read().split(',')
    titles=csv.readline().split(';')
    csv.close()