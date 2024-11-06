import os

# os.fork: プロセスの複製が可能
# if 親プロセス:
#   return 新しく生成された子プロセスのPID(プロセスID)
# else if 子プロセス:
#   return 0

pid = os.fork()

if pid > 0:
    print("Fork above 0, PID: ", os.getpid())
    print("Spawned Child's PID: ", pid)
else:
    print("Fork is 0, this is a child PID: ", os.getpid())
    print("Parent PID: ", os.getppid()) # os.getppid(): 親プロセスのPIDを返す
