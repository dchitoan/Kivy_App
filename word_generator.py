filename = "./Viet11K encoding(utf-8).txt"
# filename = "./Viet74K encoding(utf-8).txt"


def suitable(word_string: str) -> bool:
    return ("-" not in word_string) and (" " not in word_string)


def break_word(word_string: str) -> str:
    if not word_string:
        return ["", ""]
    if word_string[:2] in "gi gì gí gỉ gĩ gị qu":
        return [word_string[:2], word_string[2:]]
    nguyen_am = "a á à ả ạ ã, ă ắ ằ ẳ ẵ ặ, â ấ ầ ẩ ẫ ậ, e é è ẻ ẽ ẹ, ê ế ề ể ễ ệ, i í ì ỉ ĩ ị, o ó ò ỏ õ ọ, ô ố ồ ổ ỗ ộ, ơ ớ ờ ở ỡ ợ , u ú ù ủ ũ ụ , ư ứ ừ ử ữ ự, y ý ỳ ỷ ỹ ỵ"
    for i in range(len(word_string)):
        if word_string[i] in nguyen_am:
            break
    return (word_string[:i], word_string[i:-1])


class Word_List:
    def __init__(self) -> None:
        with open(filename, "r", encoding="utf-8") as file:
            word_list = file.readlines()
        self.word_list = [break_word(word) for word in word_list if suitable(word)]
        self.level_max = max([len(nguyenam) for _, nguyenam in self.word_list])

    def get_list(self, level):
        _list = [word for word in self.word_list if len(word[1]) <= level]
        return _list
