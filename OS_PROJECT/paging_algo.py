def fifo(pages, n, capacity):
    page_faults = 0
    str1 = ""
    top = 0
    f = []
    for i in pages:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
            else:
                f[top] = i
                top = (top + 1) % capacity
            page_faults += 1
        for j in f:
            str1 += str(j)
            str1 += ' '
        str1 += ' || '
    str1 = str1[:-3]
    return page_faults, str1


def lru(pages, n, capacity):
    f = []
    st = []
    str1 = ""
    page_faults = 0
    for i in pages:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
                st.append(len(f) - 1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            page_faults += 1
        else:
            st.append(st.pop(st.index(f.index(i))))
        for j in f:
            str1 += str(j)
            str1 += ' '
        str1 += ' || '
    str1 = str1[:-3]
    return page_faults, str1


def opr(pages, n, capacity):
    f = []
    page_faults = 0
    str1 = ""
    occur = [None for i in range(capacity)]
    for i in range(len(pages)):
        if pages[i] not in f:
            if len(f) < capacity:
                f.append(pages[i])
            else:
                for x in range(len(f)):
                    if f[x] not in pages[i + 1:]:
                        f[x] = pages[i]
                        break
                    else:
                        occur[x] = pages[i + 1:].index(f[x])
                else:
                    f[occur.index(max(occur))] = pages[i]
            page_faults += 1
        for j in f:
            str1 += str(j)
            str1 += ' '
        str1 += ' || '
    str1 = str1[:-3]
    return page_faults, str1
