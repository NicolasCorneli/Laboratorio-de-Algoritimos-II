import random
#Using write
def generate_random_numbers(amount):
    my_file = open('random-numbers.txt', 'w')
    
    for i in range(amount):
        random_number = random.randint(0, 100)
        my_file.write(str(random_number))
        my_file.write('\n')
        
    my_file.close()
#Using writelines
def generate_random_numbers_writelines(amount):
    content_list = []
    for i in range(amount):
        random_number = random.randint(0,100)
        content_list.append(str(random_number)+ "\n")
    my_file = open("random_numbers.txt" , "w")
    my_file.writelines(content_list)
    my_file.close()

def avg_with_readline():
    my_file = open("random_number.txt", "r")
    sum_of_numbers = 0
    lines_count = 0
    #Pega a primeira linha
    line = my_file.readline()
    
    while line != "":
        lines_count = lines_count + 1
        sum_of_numbers = sum_of_numbers + int(line)
        #Pega a próxima linha
        line = my_file.readline()
    
    return sum_of_numbers / lines_count
        
    

def main():
    #generate_random_numbers(100)
    #generate_random_numbers_writelines(100)
    #avg_with_readline()
main()
