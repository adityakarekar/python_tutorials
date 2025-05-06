import os
if os.path.exists("testdir"):
    for i in range(0,5):
        os.mkdir(f"testdir/Day{i+1}")
else:
    os.mkdir("testdir")
    for i in range(0,5):
        os.mkdir(f"testdir/Day{i+1}")
    print("Directory created")

