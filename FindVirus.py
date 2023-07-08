import shutil
import binascii
import os
def read_hex_file(file_path):
    with open(file_path, 'rb') as file:
        hex_data = binascii.hexlify(file.read())
        hex_string = hex_data.decode('utf-8')
        return hex_string

def save_hex_string(hex_string, output_file):
    with open(output_file, 'w') as file:
        file.write(hex_string)


ListOfPattern = []
Char2skip = ['00','26','3A','40','5C','21','2B','28','60','3C','3D','33','23','27','2D','5D','7C','5F','2A','22','7E','01','02','03','04','05','06','07','08','09','0A','0B','0C','0D','0E']

def search_in_folder():
    for i in range(20):
        Folder = f"C:\\Users\\USER\\Desktop\\AD_project\\Released\\Train\\Malware Sample\\{i}"
        for f in range(len(os.listdir(Folder))):
            while(f<(len(os.listdir(Folder)))):
                file2search = os.path.join(Folder,os.listdir(Folder)[f])
                if counter==15:
                    counter = 0
                    f+=30
                f+=1
                counter+=1
                output_file = f'TXTfiles//hex_output{f}.txt'
                hex_string = read_hex_file(file2search)
                save_hex_string(hex_string, output_file)
                txtfile = open(f"C:\\Users\\USER\\Desktop\\AD_project\\TXTfiles\\hex_output{f}.txt", "r")
                data = txtfile.read()
                k=0
                findpattern = ""
                while(k<len(data)-2):
                    x = data[k:k+2]
                    if x in Char2skip: 
                        k+=2
                        if(len(findpattern)>5):
                            with open(f"C:\Users\USER\Desktop\AD_project\PatternOfFolders\{i}.txt",'a') as file:
                                file.writelines(findpattern)
                                findpattern = ""
                        
                    else:
                        if (len(findpattern)>=25):
                            with open(f"C:\Users\USER\Desktop\AD_project\PatternOfFolders\{i}.txt",'a') as file:
                                file.writelines(findpattern)
                                findpattern = ""

                        findpattern+=x
                        k+=2

                    

def FindCommon():
    Folder = "C:\Users\USER\Desktop\AD_project\PatternOfFolders"
    for f in range(len(os.listdir(Folder))):
            while(f<(len(os.listdir(Folder)))): 
                file2search = os.path.join(Folder,os.listdir(Folder)[f])
    with open(file2search) as f:
        data = f.readlines()
    for line in data:
        count = 0
        for checkline in data:
            if (line == checkline):
                count+=1
        if (count>=50):
            if line not in ListOfPattern:
                ListOfPattern.append(line)
            

def DeletePattern():
    Folder = "C:\Users\USER\Desktop\AD_project\Released\Train\Benign"
    for f in os.listdir(Folder):
        count = 0
        for p in ListOfPattern:
            if p in f:
                count+=1
        if (count>=2):
            ListOfPattern.remove(p)

        
def CheckFile(FileTocheck):
    f = open(FileTocheck, "r")
    data = f.read()
    for p in ListOfPattern:
        for d in data:
            index = 0
            for i in range(0,len(p)):
                if(d==p[i]):
                    index += 1
                else:
                    break
            if (index == len(p)):
                return True
    return False

#pre proccess
search_in_folder()
FindCommon()
DeletePattern()