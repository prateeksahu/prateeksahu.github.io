#! /usr/bin/env python3
import subprocess
def main():
    for i in range(10):
        s,o = subprocess.getstatusoutput("curl localhost:30333/")
        for line in o.split("\n"):
            if "My hostname is" in line:
                print(line[5:47])
if __name__ == "__main__":
    main()
