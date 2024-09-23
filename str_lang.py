import os

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
    lang_code = 'zh_tw'  # 語言代碼，例如 zh 代表中文
    translated_string = translate(input_string, lang_code)
    print(translated_string)
