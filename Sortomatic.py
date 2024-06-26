import os
from PIL import Image

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size

def sort_images_by_size(directory):
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    images_with_sizes = [(get_image_size(os.path.join(directory, img)), img) for img in image_files]
    
    sorted_images = sorted(images_with_sizes, key=lambda x: x[0][0] * x[0][1], reverse=True)
    
    sorted_filenames = [img[1] for img in sorted_images]
    
    return sorted_filenames

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_console()

    ascii_art = """
\033[93m                                                                                                        
  .--.--.                          ___                       ____                ___                        
 /  /    '.                      ,--.'|_                   ,'  , `.            ,--.'|_    ,--,              
|  :  /`. /    ,---.    __  ,-.  |  | :,'   ,---.       ,-+-,.' _ |            |  | :,' ,--.'|              
;  |  |--`    '   ,'\ ,' ,'/ /|  :  : ' :  '   ,'\   ,-+-. ;   , ||            :  : ' : |  |,               
|  :  ;_     /   /   |'  | |' |.;__,'  /  /   /   | ,--.'|'   |  || ,--.--.  .;__,'  /  `--'_       ,---.   
 \  \    `. .   ; ,. :|  |   ,'|  |   |  .   ; ,. :|   |  ,', |  |,/       \ |  |   |   ,' ,'|     /     \  
  `----.   \'   | |: :'  :  /  :__,'| :  '   | |: :|   | /  | |--'.--.  .-. |:__,'| :   '  | |    /    / '  
  __ \  \  |'   | .; :|  | '     '  : |__'   | .; :|   : |  | ,    \__\/: . .  '  : |__ |  | :   .    ' /   
 /  /`--'  /|   :    |;  : |     |  | '.'|   :    ||   : |  |/     ," .--.; |  |  | '.'|'  : |__ '   ; :__  
'--'.     /  \   \  / |  , ;     ;  :    ;\   \  / |   | |`-'     /  /  ,.  |  ;  :    ;|  | '.'|'   | '.'| 
  `--'---'    `----'   ---'      |  ,   /  `----'  |   ;/        ;  :   .'   \ |  ,   / ;  :    ;|   :    : 
                                  ---`-'           '---'         |  ,     .-./  ---`-'  |  ,   /  \   \  /  
                                                                  `--`---'               ---`-'    `----'     
\033[0m"""

    separator_line = "=" * 120

    print(ascii_art)
    
    print("\n\033[91mMade by Cheddlar\033[0m")

    print(separator_line)

    print()

    directory_path = input("Please enter the directory path: ")

    sorted_images = sort_images_by_size(directory_path)

    for image in sorted_images:
        print(image)

    input("Press Enter to continue...")
