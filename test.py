from array import array


array_2D = [[0,0], [0,0]]
array_2D = [[0,0]]*2
array_1D = [0,0]

# # print(array_2D)
# # print(array_1D)


# for i, verdi in enumerate(array_1D):

#     print(i)
#     print(verdi)

# number_of_points = [4,6]
# cluster_point_sum = [[30,15],[20,19]]

# new_centroids = []


# for i, num in enumerate(number_of_points):

#     centroid_x = cluster_point_sum[i][0] / num
#     centroid_y = cluster_point_sum[i][0] / num

#     new_centroids.append([centroid_x, centroid_y])

# print(new_centroids)

# for i in len(cluster_point_sum):
#     print(i)

pred = [0,1,1,1,0]


# for index_of_point, index_of_closest_centroid in enumerate(pred):

#     array_2D[index_of_closest_centroid][0] += 1
#     # array_2D[index_of_closest_centroid][1] += 1

#     array_1D[index_of_closest_centroid] += 1

array_2D[0][0] = 1

print(array_1D)
print(array_2D)

