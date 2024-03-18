import os
base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


target_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')


with open(target_path, 'r') as f:
    print(f.read())