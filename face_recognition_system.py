import subprocess


def execShellCommand(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,executable="/bin/bash")

    while True:  
        buff = p.stdout.readline()  
        if buff == '' and p.poll() != None:  
            break
    p.wait()
 
 
def main():
    cmd = 'source ~/.profile' + '&&' + 'workon cv' + '&&' + 'python face_recognition.py'
    execShellCommand(cmd)
    
if __name__ == "__main__":
    while(True):
        choose = raw_input('choose')  #得到用户按下的按钮请求是什么，还要详细描述
        if choose == 'r':
            main()
        else:
            print('thanks')
            break
        
    