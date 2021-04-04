import logging
import random
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='myAppLog.txt', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')


def loop():
    raise Exception

functions = ["getUser" ,"getAlert", "uploadLog", "searchLog", "addUser", "createSite", "changeTheme"]
servicenames = ["apigateway", "logparser", "logreader", "logcompresser", "mlservice"]
actions = [" uploaded a file from Google cloud API "," failed to run fucntion ", " scheduled to run fucntion ", " starts to run fucntion ", " finished running fucntion ", " uploaded a file from AWS API "]


accessKey = input("Example access key:\n")
logging.debug("User uid " + str(random.randrange(1,10000,1)) + " uploaded a file using AWS access key " + accessKey)