import schedule
import time
from report import generate_sales_report


def job():
    try:
        print("Running scheduled job...")
        generate_sales_report()
        print("Job completed successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

RUN_TIME = "13:12" 

schedule.every().day.at(RUN_TIME).do(job)


if __name__ == "__main__":
    print(f"Scheduler started. Job will run daily at {RUN_TIME}")
    while True:
        schedule.run_pending()
        time.sleep(1)