filename = "./Viet11K encoding(utf-8).txt"
# filename = "./Viet74K encoding(utf-8).txt"

import re


def suitable(word_string: str) -> bool:
    return ("-" not in word_string) and (" " not in word_string)


def break_word(word_string: str) -> str:
    if not word_string:
        return ["", "", ""]
    if word_string[:2] in "gi gì gí gỉ gĩ gị qu":
        i = 2
    else:
        nguyen_am_chuan = (
            "aáàảạãăắằẳẵặâấầẩẫậeéèẻẽẹêếềểễệiíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵ"
        )
        for i in range(len(word_string)):
            if word_string[i] in nguyen_am_chuan:
                break
    phu_am = word_string[:i]
    nguyen_am = remove_dau_thanh(word_string[i:])
    return (word_string, phu_am, nguyen_am)


def remove_dau_thanh(u_str):
    INTAB = "aạảãàáâậầấẩẫăắằặẳẵoóòọõỏôộổỗồốơờớợởỡeéèẻẹẽêếềệểễuúùụủũưựữửừứiíìịỉĩyýỳỷỵỹ"
    OUTTAB = "aaaaaaââââââăăăăăăooooooôôôôôôơơơơơơeeeeeeêêêêêêuuuuuuưưưưưưiiiiiiyyyyyy"
    r = re.compile("|".join(INTAB))
    replaces_dict = dict(zip(INTAB, OUTTAB))
    return r.sub(lambda m: replaces_dict[m.group(0)], u_str)


class Word_List:
    def __init__(self) -> None:
        with open(filename, "r", encoding="utf-8") as file:
            word_list = file.read().split()
        self.word_list = [break_word(word) for word in word_list if suitable(word)]
        self.level_max = max([len(nguyenam) for _, _, nguyenam in self.word_list])

    def get_list(self, level=0):
        if level == 0:
            level = self.level_max
        _list = [word for word in self.word_list if len(word[2]) <= level]
        return _list


# wl = Word_List()
# words = wl.get_list()
# print([word for word in words if len(word[2]) == wl.level_max])
# print(wl.level_max)
# print(len(words))
