import os

#====================設定檔案===================
lang_code = 'zh_tw'  # 語言代碼，例如 zh 代表中文
BLACK_PIECE = '\033[90m'  # 亮黑色（灰色）
RED_PIECE = '\033[31m'           # 紅色
RESET_COLOR = '\033[0m'          # 重置顏色

def load_translation(lang_file):
    translations = {}
    try:
        with open(lang_file, 'r', encoding='utf-8') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    translations[key] = value
    except FileNotFoundError:
        print(f"File {lang_file} not found.")
    return translations

def replace_string_with_translation(input_string, translations):
    for key, value in translations.items():
        input_string = input_string.replace(key, value)
    return input_string

def translate(input_string, lang_code):
    # 假設 lang 資料夾在當前工作目錄下
    lang_folder = os.path.join(os.getcwd(), 'lang')
    lang_file = os.path.join(lang_folder, f'{lang_code}.txt')
    
    # 讀取翻譯字典
    translations = load_translation(lang_file)
    
    # 替換字串
    return replace_string_with_translation(input_string, translations)

def label_print(input_string):
    translated_string = translate(input_string, lang_code)
    print(translated_string)

def c_label_print(input_string,color):
    translated_string = translate(input_string, lang_code)
    if (color=='R'):
        print( RED_PIECE + translated_string + RESET_COLOR )
    elif (color=='B'):
        print( BLACK_PIECE + translated_string + RESET_COLOR )
