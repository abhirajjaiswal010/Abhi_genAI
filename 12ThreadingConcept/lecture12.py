#process queue

from multiprocessing import Process,Queue

def prepareChai(queue):
    queue.put("Masala Chai is ready")



if __name__=="__main__":
    queue=Queue()
    p=Process(target=prepareChai,args=(queue,))
    p.start()
    p.join()
    print(queue.get())
