import time
import multiprocessing as mp
import random
import numpy as np
import keyboard

def f(a):
    n = 10000
    matrix_a = [ [ random.random() for i in range(n) ] for j in range(n) ]
    matrix_b = [ [ random.random() for i in range(n) ] for j in range(n) ]
    matrix_c = [ [ 0 for i in range(n) ] for j in range(n) ]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_c = matrix_c + (np.array(matrix_a)[i,k] * np.array(matrix_b)[k,j])

if __name__ == '__main__':
    print("CPU count: " + str(mp.cpu_count()))
    print("Program started. Press 'c' to stop")
    worker = mp.Process(target=f, args=("test",))    
    print("Starting matrix process")
    try:
        worker.start()
        start = time.perf_counter()
        print("Matrix process started")
        while(worker.is_alive()):
            if(keyboard.is_pressed('c')):
                worker.terminate()
                print("Matrix process stopped")
            time.sleep(0.01)
        worker.join()
    except mp.ProcessError:
        print("Exception: Processor Error")
    stop = time.perf_counter()
    print("Matrix process done in: " + str(stop - start))
    worker.close()
    print("Program stopped")