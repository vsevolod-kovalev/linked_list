from linked_list.llist import LList

if __name__ == "__main__":
    l = LList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.prepend(10)
    l.print()
    print("\n")
    l.reverse()
    l.print()
    print()
    print(l.middle().data)
    print(l.get_length())