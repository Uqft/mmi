import csv
import ast

def csv_create():
    header = [["user_name", "command", "container_id", "time"]]
    logCSV = open('metric.csv', 'w')
    with logCSV:
        writer = csv.writer(logCSV)
        writer.writerows(header)

def readlastline(f):
    f.seek(-2, 2)  
    while f.read(1) != b"\n":  
        f.seek(-2, 1)  
    lastline = f.read()
    lastline = lastline.decode("UTF-8")
    lastline = ast.literal_eval(lastline)
    return lastline  

def txtlog_reading():
    with open('events.txt',"r") as f:
        lines_list=[]
        for line in f:
            lines_list.append(line)
        return lines_list

def main():
    message_list = txtlog_reading()
    log_list = []
    #print(message_list[0])
    #print(type(ast.literal_eval(message_list[0])))

    for i in range(len(message_list)):
        message = ast.literal_eval(message_list[i])

        user_name = message["output_fields"]["user.name"]
        # print(user_name)
        if user_name == "root":
            user_name = 1
        else:
            user_name = 0

        command = message["output_fields"]["proc.name"]
        # print(command)
        if command == "sudo":
            command = 1
        else:
            command = 0

        container_id = message["output_fields"]["container.id"]
        # print(container_id)
        if container_id == "host":
            container_id = 1
        else:
            container_id = 0

        behavior = "Norm"
        
        log = [[user_name, command, container_id, behavior]]
        if log in log_list:
            print("This message in log already")
            pass
        else:
            log_list.append(log)
            logCSV = open('metric.csv', 'a')
            with logCSV:
                writer = csv.writer(logCSV)
                writer.writerows(log)
        
if __name__ == '__main__':
    # csv_create()
    main()
