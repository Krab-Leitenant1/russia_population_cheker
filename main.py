from parser import Parser

import schedule
def main():
    p = Parser('db', 'https://www.worldometers.info/world-population/russia-population/')
    p.setup()
    schedule.every().day.at("12:00").do(p.parse)
    while True:
        schedule.run_pending()
if __name__ == "__main__":
    main()

