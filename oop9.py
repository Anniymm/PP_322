# პარალელური და მრავალგანშტოებიანი პროგრამირება

# პარალელური პროგრამირება - მოქმედებების შესრულება ერთდროულად (პარალელურად)

# პარალელური - ერთდროულად გავუშვა თასქები ერთმანეთის პარალელურად
# Concurrency - იმდენად სწრაფად ენაცვლება მოქმედებები ერთმანეთს რომ ილუზია იქმნება რომ 
# ერთდროულად სრულდება (multitasking)


# thread - ნაკადი 
# multi-threading - მრავალგანშტოებიანი პროგრამირება - არის გზა რომ მივაღწიო პარალელიზმს.

# -----------------------------------------------------------------------------------
# import time
# # multiprocessing -> Process
# from multiprocessing import Process

# def task(name):
#     print(f"Task {name} started")
#     time.sleep(2)
#     print(f"Task {name} stopped")

# if __name__ == "__main__":
#     p1 = Process(target = task, args = ("P1",))
#     p2 = Process(target = task, args = ("P2",))

#     p1.start() # -> pirveli procesis dawyeba
#     p2.start()

#     p1.join() # -> pirvel process davelodot rom dasruldes
#     p2.join()

#     print("Both tasks completed")
#es davaleba aris paralelizmze 

# ------------------------------------------------------------------------------------------------------

# import threading  # Thread
# # from threading import Thread
# import time 

# def worker():
#     print("thread started")
#     time.sleep(2)
#     print("thread finished")


# t = threading.Thread(target = worker)
# t.start()
# t.join()
# print("program finished ")

# ------------------------------------------------------------------------------------------------------

# threadebis sinqronizacia

# thread1 <- data -> thread2      ----> Lock

# import threading

# # globaluri cvladi romelic yvela threads whirdeba 
# counter = 0 

# #Thread, Lock
# lock = threading.Lock()   # lockis objectis sheqmna 

# def increment():
#     global counter 
#     for _ in range(1000):
#         lock.acquire() # -> davlocke saziaro resursebi
#         counter += 1 
#         lock.release()

# threads = [threading.Thread(target=increment) for _ in range(2)]
# # [thread1 -> incrementtan, thread2-> incrementtan]
# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# print('counter', counter)

# ---------------------------------------------------------------------------------------------------

# import threading 
# import time

# bank_balance = 100
# lock = threading.Lock()

# def deposit(amount, thread_name):
#     global bank_balance 

#     for _ in range(5):
#         lock.acquire()
#         print(f'{thread_name} depositing {amount}.....')

#         current = bank_balance # mimdinare balasi waikitxos
#         time.sleep(1)
#         bank_balance = current + amount # update

#         print(f'{thread_name} New balance: {bank_balance}')

#         lock.release()
#         time.sleep(1)

# t1 = threading.Thread(target=deposit, args= (50, "Thread_1"))
# t2 = threading.Thread(target=deposit, args= (70, "Thread_2"))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"bank final balance {bank_balance}")


# -----------------------------------------------------------------------------------------------------

