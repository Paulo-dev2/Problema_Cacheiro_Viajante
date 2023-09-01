# Print iterations progress
def printProgressBar (iteration, total, suffix = ''):

    percent = ("{0:.2f}").format(100 * (iteration / float(total)))
    filledLength = int(100 * iteration // total)
    bar = '█' * filledLength + '-' * (100 - filledLength)
    print(f'\r |{bar}| {percent}%', end = '\r')