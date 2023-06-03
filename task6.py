def exponential_filter(alpha, data):
    filtered_data = [data[0]]
    for i in range(1, len(data)):
        filtered_data.append(alpha * data[i] + (1 - alpha) * filtered_data[i-1])
    return filtered_data

alpha = 0.2
data = [1, 2, 3, 4, 5, 4, 3, 2, 1]
filtered_data = exponential_filter(alpha, data)

print("Исходные данные: ", data)
print("Отфильтрованные данные: ", filtered_data)