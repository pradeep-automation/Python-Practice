with open("my_news.txt", 'r') as file:
    stmt = file.read()

    # print(stmt)
    st = stmt.casefold()
    ls = st.split()
    my_dic = {}

    for item in ls:
        if item in my_dic:
            my_dic[item]  += 1
        else:
            my_dic[item] = 1



    print(my_dic.pop("microsoft"))