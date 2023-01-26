import schedule
import time
from process import desuso
from app import ProcesoDesuso

def all():
    ProcesoDesuso()




if __name__ == '__main__':
    schedule.every().day.at("00:00").do(all)
    while True:
        schedule.run_pending()
        time.sleep(1)
