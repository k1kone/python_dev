lis = ["A", "B", "C", "D", "E"]

print("del list[1]")
lis_del = lis
del lis_del[1] #[x:y] x〜yまでなど部分指定も可能
print(lis_del) #"B"が削除されます


print("\n\nlist.pop(1)")
lis_pop = lis
lis_pop.pop(1) #引数を省略すると最後の要素が削除されます。
print(lis_pop)


print("\n\nlist.remove('指定の値')")
lis_remove = lis
lis_remove.remove("D")
print(lis_remove)
