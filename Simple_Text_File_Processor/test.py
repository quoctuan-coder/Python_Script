

def processing():
    file_txt = 'Simple_Text_File_Processor/filename01.txt'
    file_wxt = 'Simple_Text_File_Processor/filename01.wxt'
    lines_txt = open(file_txt).readlines()
    lines_wxt = open(file_wxt).readlines()

    print(lines_txt)

def generate_rxt():
    file_txt = 'Simple_Text_File_Processor/filename01.txt'
    out_file = 'Simple_Text_File_Processor/out_filename01.rxt'
    out_write = open(out_file,'w')
    add_character = ''
    lines_txt = open(file_txt).readlines()
    index = -1
    number_character = 1
    for cnt,line in enumerate(lines_txt):
        if (cnt % 26 == 0 and cnt != 0):
            number_character = cnt // 26 + 1
            index = 0
        else:
            index = index + 1
            number_character = cnt // 26 + 1

        if number_character == 1:
            add_character = chr(97+index)
        elif number_character >= 2:
            add_character = chr(97+number_character-2) + chr(97+index)
        
        out_line = line.replace('\n','') + '\t' + add_character + '\n'
        out_write.write(out_line)
    
    out_write.close()

def generate_sxt():
    file_txt = 'Simple_Text_File_Processor/filename01.txt'
    file_wxt = 'Simple_Text_File_Processor/filename01.wxt'
    lines_txt = open(file_txt).readlines()
    lines_wxt = open(file_wxt).readlines()
    out_file = 'Simple_Text_File_Processor/out_filename01.sxt'
    out_write = open(out_file,'w')

    # print(lines_txt)
    for cnt,line in enumerate(lines_txt):
        line = line.replace('\n','').split('\t')[0]
        origin_digits = line.split('.')[0]
        get_three_digits = line.split('.')[1]
        current_convert = ('{},{}'.format(convert2seconds(int(origin_digits)),get_three_digits[0:3]))
        
        if cnt == 0:
            previous_convert = current_convert
            continue

        out_line = '{} --> {}\n'.format(previous_convert,current_convert)
        previous_convert = current_convert

        out_write.write(out_line)
    out_write.close


def convert2seconds(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    ret = '{}:{}:{}'.format(str(hour).zfill(2),str(minutes).zfill(2),str(seconds).zfill(2))
    return ret

generate_sxt()



