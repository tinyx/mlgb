import future
import glob


for txt_file_name in glob.glob("samples/*.txt"):
    with open(txt_file_name, 'r') as txt_file:
        for line in txt_file:
            print(line)

