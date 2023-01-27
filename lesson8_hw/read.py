import csv

def read_file_words(filename):
    s = open(f"lesson8_hw/random/{filename}.txt", "r",encoding='utf-8')
    out=s.read().split(',')
    s.close()
    return out