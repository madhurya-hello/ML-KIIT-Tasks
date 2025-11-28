import csv
import random

def generate_dataset():
    
    filename = 'student_data.csv'
    headers = ['name', 'roll', 'marks', 'age', 'height']
    first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

    data = []

    for i in range(1, 21):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        roll = i  
        marks = random.randint(0, 100)
        age = random.randint(18, 45) 
        height = random.randint(150, 190) 

        data.append([name, roll, marks, age, height])

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)
                            
    except IOError as e:
        print(f"Erro")

if __name__ == "__main__":
    generate_dataset()