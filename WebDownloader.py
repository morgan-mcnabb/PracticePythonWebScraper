import requests

# get the file from the website
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    # Check if the GET request fails
    res.raise_for_status()

    # create new file and write to it in 'write binary (wb) mode
    # to save to hard drive
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print('There was a problem: %s' % exc)
