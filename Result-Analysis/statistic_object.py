import numpy as np
from matplotlib import pyplot as plt


#20 types
basic_type = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car',
              'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike',
              'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
def polish_str2list(str):
    str = str.replace('[', '')
    str = str.replace(']', '')
    str = str.replace(' ', '')
    str = str.replace('-', '')
    strlist = str.split('.')[:-1]
    return strlist

def check_error_type(results = []):
    ""
    "input is an list 3 elements with"
    "filename, groundString, predictString"
    "return tuple(wrong_type, filename)"
    "1:没predict到的 "
    #typeNo2 == 0

    "2:predict类别完全不正确 "
    #count01 == 0

    "3:predict类别部分正确 多和少预测类别都可以判断"
    "typeNo1 typeNo2"
    "count01- truth中被predict到的类别数 严格小于等于 typeNo1"
    "count02- predict中属于truth的类别数 严格小于等于 typeNo2"
    "count01 < typeNo1 少 31-3"
    "count02 < typeNo2 多 32-4"
    "若同时出现则有少有多  33-5"

    "6.predict类别全部正确但数量不正确 返回不正确类别及数量差"
    "dict[i] != dict[j]"

    "7.predict类别和数量都正确 "
    "7种应该概括了所有分类 "

    "extra 0:数量正确 类别不正确的"

    print (results)
    objNo1, typeNo1, dict1 = dict_count(results[1])
    objNo2, typeNo2, dict2 = dict_count(results[2])
    # Type1
    if typeNo1 > 0 and typeNo2 == 0:
        return (1, results[0])
    # Type2-7
    count01 = 0
    count_accurate = {}
    count_accurate[-1] = 0
    for i in dict1:
        #total accumulate
        total_label[i] += dict1[i]
        if dict1[i] > 0:
            if dict2[i] > 0:
                count01 = count01 + 1
                if dict2[i] == dict1[i]:
                   #true predict
                   predict_true[i] += dict2[i]
                   count_accurate[i] = 0
                else :
                   count_accurate[-1] = 1
                   # nega: predict more; pos: pred less
                   if abs(dict1[i] - dict2[i]) > 0:
                       count_accurate[basic_type[i]] = dict1[i] - dict2[i]
    count02 = 0
    for i in dict2:
        if dict2[i] > 0:
            if dict1[i] > 0:
                count02 += 1

    #calculate accuary rate


    # Type0
    # if objNo1 == objNo2:
    #     if count01 < typeNo1 or count_accurate[-1] == 1:
    #         return (0, results[0])
    #2
    if count01 == 0:
        return (2, results[0])
    #33-5
    if count01 < typeNo1 and count02 < typeNo2:
        return (5, results[0])
    #31-3
    if count01 < typeNo1:
        return (3, results[0])
    #32-4
    if count02 < typeNo2:
        return (4, results[0])
    #6
    if count_accurate[-1] == 1:
        return (6, results[0], count_accurate)
    return (7, results[0])
# statistic objNo, typeNo
def dict_count(array):
    dict = {}
    objNo = 0
    typeNo = 0
    for a in range(len(array)):
        count = int(array[a])
        if count > 0:
            objNo += count
            typeNo += 1
        dict[a] = count
    return objNo, typeNo, dict

# PT/tot = acc_rate PW/tot = false_rate
predict_true = [0]*20
#predict_wrong = [0]*20
total_label = [0]*20
if __name__ == '__main__':
    results = []
    #initialize error_result in [0-5]
    error_result = {}
    for i in range(8):
        error_result[i] = []
    with open("all_ones.txt") as file:
        count = 0
        times = -1
        for line in file:
            if count % 9 == 0:
                if times > -1:
                    print(results[times][1])
                    for i in range(len(results[times][1])):
                        total_label[i] += int(results[times][1][i])
                        predict_true[i] += min(int(results[times][1][i]),int(results[times][2][i]))
                results.append([])
                times += 1
            if count % 9 == 1:
                line = line.replace('\n','')
                results[times].append(line)
            if count % 9 == 3:
                str1 = polish_str2list(line)
                results[times].append(str1)
            if count % 9 == 4 and line != 'prediction:\n':
                str3 =  polish_str2list(line)
                str1 += str3
                del  str3
                count -= 1
            if count % 9 == 5:
                str2 = polish_str2list(line)
            if count % 9 == 6:
                str3 =  polish_str2list(line)
                str2 += str3
                del str3
                results[times].append(str2)
            count += 1
    print(results[3:10])
    print(times)

    truth = np.array(total_label)
    pred_true = np.array(predict_true)
    accuracy = predict_true/truth

    print(truth)
    print(pred_true)
    print(accuracy)
    print(np.sum(pred_true)/np.sum(truth))






