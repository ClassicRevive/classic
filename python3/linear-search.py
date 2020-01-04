list1 = ["they bought a car, in car. nashville car", "hello world car nashville tbone",
         "this is such a hard program to make like damn bruh car -_-"]


def word_search(doclist, keyword):
    """
    parse through the doclist assigning i as index and doc as a value in doclist.
    clean the values by first splitting them up into words and then strip periods and commas and
    assigning lower case. now check if the keyword is present in this list of cleaned words
    """
    indices = []

    for i, doc in enumerate(doclist):
        splits1 = doc.split()
        cleaned = [splits.strip(".,#\'\'#[;#[;.").lower() for splits in splits1]

        if keyword in cleaned:
            indices.append(i)

    return indices


print(word_search(list1, "car"))


def multiple_word_search(doclist, keywords):
    finds = {}
    for keyword in keywords:
        finds[keyword] = word_search(doclist, keyword)

    return finds



print(multiple_word_search(list1, ["car", "nashville"]))
