import numpy as np

# numpy version
mid_score = np.array([10, 20, 30])
final_score = np.array([70, 80, 90])

total = mid_score + final_score
# print(total)
print(f'시험성적 합계 : {total}')
print(f'시럼성적 평균 : {total / 2}')


# python version
# mid_score = [10, 20, 30]
# final_score = [70, 80, 90]
#
# total = list()
#
# for i in range(len(mid_score)):
#     total.append(mid_score[i] + final_score[i])
#
# average = [int(total[i]/2) for i in range(len(mid_score))]
# print(f'시험성적 합계 : {total}')
# print(f'시험성적 평균 : {average}')
