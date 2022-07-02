from pypinyin import pinyin, Style

def get_references(path: str) -> list:
    res = []
    with open(path, mode='r', encoding="utf-8") as f:
        for line in f.readlines():
            res.append(line)
    return res

def get_output(refs: list):
    with open("output.txt", mode='w', encoding='utf-8') as f:
        for ref in refs:
            f.write(ref)

if __name__ == '__main__':
    path = "input.txt"
    reference = get_references(path)
    reference.sort(key=lambda keys:[pinyin(i, style=Style.TONE3) for i in keys])
    get_output(reference)