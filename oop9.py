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

import threading 
import time 