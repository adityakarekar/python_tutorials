import os
if os.path.exists("testdir"):
    for i in range(0,5):
        os.rename(f"testdir/Day{i+1}",f"testdir/Tutorial{i+1}")
else:
    os.mkdir("testdir")
    print("Directory created")