import json
json_open = open("lpic.json","r",encoding="utf-8")
json_load = json.load(json_open)
com_list = [i for i in json_load]

def com_search(com):
    print(f"command: {com}")
    coms = com.split()
    if not coms[0] in com_list:
        print("指定されたコマンドは見つかりませんでした。")
        return
    if len(coms) > 1:
        for json_key in json_load[coms[0]]:
            descriptions = [com for com in json_load[coms[0]][json_key] if coms[1] in com]
        if descriptions:
            print("--",json_key)
            for description in descriptions:
                print(description)
        else:
            print(" \n---指定されたオプションは見つかりませんでした。---\n")
            print(f"command: {coms[0]}")
            com_info(coms)
        return
    elif len(coms) == 1:
        com_info(coms)

def com_info(coms):
    for json_key in json_load[coms[0]]:
        print("--",json_key)
        for i in json_load[coms[0]][json_key]:
            print(i)

def com_letter_search(com_letter):
    com_list = [i for i in json_load if i[0]== com_letter]
    for com in com_list:
        print(com)

loop_switch = "loop"
while loop_switch == "loop":
    try:
        print("モードを選択してください。")
        mode = int(input("0:ファイルに登録されているコマンド一覧 1:コマンド検索　2:コマンドの頭文字からコマンド検索 3:exit\n 入力:"))
        if int(mode) == 3:
            print("------------------")
            print("プログラムを終了します。")
            print("------------------")
            break
    except ValueError:
        print("\n半角数字のみ使用できます。\n")
    while loop_switch == "loop":
        if int(mode) > 0:
            print("\ncexit で現在のモードを終了します。\n")
        if int(mode) == 0:
            print("------------------")
            for com in com_list:
                print(com)
            print("------------------")
            break
        elif int(mode) == 1:
            print("------------------")
            com = input("コマンドを入力してください。")
            if com == "cexit":
                break
            com_search(com)
            print("------------------")
        elif int(mode) == 2:
            print("------------------")
            com_letter = input("検索したいコマンドの頭文字を入力して下さい。")
            if com_letter == "cexit":
                break
            com_letter_search(com_letter)
            print("------------------")
        else:
            print("指定した選択肢はありません。")

