with open("my_news.txt", 'r') as file:
    stmt = file.read()

    # print(stmt)
    st = stmt.casefold()
    ls = st.split()
    my_dic = {}

    for item in ls:
        # my_dic[item] = my_dic.setdefault(item, 0) + 1
        my_dic[item] = my_dic.get(item, 0) + 1
        # if item in my_dic:
        #     my_dic[item] += 1

        # else:
        #     my_dic[item] = 1

print(my_dic)
# print(my_dic["the"])
# print(my_dic.pop("the"))


