import sys, time

def clear():
	with open("latestLog.txt", "w") as log:
		log.write("")

def print(*args, **kwargs):
	sys.stdout.write(f"{''.join(map(str,args))}\n")

	with open("latestLog.txt", "a") as log:
		log.write(f"{time.time()}: {''.join(map(str,args))}\n")