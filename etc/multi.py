# multithreading 을 사용함, 물리적으로 cpu 코어를 활용하여 병렬처리
import multiprocessing
import time as t

def long_task():
    for w in range(5):
        print(f"일하는 중...{w+1}")
        t.sleep(1)

if __name__ == "__main__":
    start = t.time()
    print("=====Start=====")
    processes = []
    for n in range(5):
        p= multiprocessing.Process(target=long_task)
        processes.append(p)
    for p in processes:
        p.start() # 쓰레드 시작
    for p in processes:
        p.join() # 쓰레드 종료될 때 까지 기다림 (= waiting)
    print("=====끝=====")
    print(f"총 소요시간: {t.time() - start:.2f}초")