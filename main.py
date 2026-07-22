from parser import Parser
import sys
import schedule
import subprocess

def main():
    front = subprocess.Popen([sys.executable, 'front.py'], stdout=subprocess.PIPE)


    p = Parser('db', 'https://www.worldometers.info/world-population/russia-population/')

    p.setup()


    schedule.every().day.at("12:15").do(p.parse)
    while True:

        schedule.run_pending()

        if front.poll()!=None:
            sys.exit(0)


if __name__ == "__main__":
    main()

