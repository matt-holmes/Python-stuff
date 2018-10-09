import threading
import time

num_of_threads = 1010
acc_balance = 10000
lock = threading.Lock()

def subtract_ten_from_balance():
    global bal, acc_balance
    bal = acc_balance
    with lock:
        if(acc_balance < 10):
            return None
        else:
            time.sleep(0.0000000000001)
            bal -= 10
            acc_balance = bal


def run_experiment():
    threads = []
    for i in range(num_of_threads):
        t = threading.Thread(target=subtract_ten_from_balance)
        threads.append(t)
        t.start()

    for i in threads:
        i.join()

    print("Account balance: {0}".format(acc_balance))

run_experiment()
