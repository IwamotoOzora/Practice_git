test_scores = {"network":60, "database":80, "security": 50}
print(test_scores)

pick_database_data = test_scores["database"]
print(pick_database_data)

test_scores["programing"] = 65
test_scores["security"] = 55
print(test_scores)

del test_scores["security"]
print(test_scores)

scores = (70, 80, 55, 33)
print(scores)
print(scores[-1])
element_scores_count = len(scores)
print("要素数は{}".format(element_scores_count))
scores_total = sum(scores)
print("合計は{}".format(scores_total))

scores = {70, 80, 90 ,50}
scores.add(80)
print(scores)
print("要素数は{}".format(len(scores)))
print("合計は{}".format(sum(scores)))

members = ["岩本", "村下", "川辺", "山田"]
print(tuple(members))
print(list(scores))
print(set(test_scores.values()))

member_hobbies = {
    "松田": {"SNS", "麻雀", "自転車"},
    "浅木": {"麻雀", "食べ歩き", "数学"}
}
common_hobbies = member_hobbies["松田"] & member_hobbies["浅木"]
print(common_hobbies)

print(scores)
print("開始")
print("終了")