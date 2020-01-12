from reconstruction import get_hidden_point_from_ids, save_points, read_two_camera_points

def slika2(src, dest):
    points = read_two_camera_points(src)

    # skrivena tacka 5
    camera1_point5 = [328, 292, 1]
    camera2_point5 = get_hidden_point_from_ids(points, [4, 1, 3, 2, 4, 8, 3, 7, 8, 1], 1)
    points[5] = [camera1_point5, camera2_point5]

    # skrivena tacka 6
    camera1_point6 = get_hidden_point_from_ids(points, [5, 1, 8, 4, 4, 3, 8, 7, 5, 7], 0)
    camera2_point6 = get_hidden_point_from_ids(points, [5, 1, 8, 4, 4, 3, 8, 7, 5, 7], 1)
    points[6] = [camera1_point6, camera2_point6]


    camera2_point14 = [714, 564, 1]
    points[14] = [[], camera2_point14]

    camera2_point10 = [711, 335, 1]
    points[10] = [[], camera2_point10]

    # skrivena tacka 13
    camera1_point13 = [266, 586, 1]
    camera2_point13 = get_hidden_point_from_ids(points, [11, 10, 15, 14, 11, 12, 15, 16, 16, 14], 1)
    points[13] = [camera1_point13, camera2_point13]
    
    # skrivena tacka 10
    camera1_point10 = get_hidden_point_from_ids(points, [12, 11, 16, 15, 12, 9, 16, 13, 9, 11], 0)
    points[10][0] = camera1_point10

    # skrivena tacka 14
    camera1_point14 = get_hidden_point_from_ids(points, [12, 11, 9, 10, 16, 13, 12, 9, 13, 15], 0)
    points[14][0] = camera1_point14

    
    # skrivena tacka 18
    camera1_point18 = get_hidden_point_from_ids(points, [20, 17, 24, 21, 20, 19, 24, 23, 19, 17], 0)
    camera2_point18 = get_hidden_point_from_ids(points, [20, 17, 24, 21, 20, 19, 24, 23, 19, 17], 1)
    points[18] = [camera1_point18, camera2_point18]

    
    # skrivena tacka 22
    camera1_point22 = get_hidden_point_from_ids(points, [20, 17, 24, 21, 20, 19, 24, 23, 23, 21], 0)
    camera2_point22 = get_hidden_point_from_ids(points, [20, 17, 24, 21, 20, 19, 24, 23, 23, 21], 1)
    points[22] = [camera1_point22, camera2_point22]

    save_points(points, dest)

def slika1(src_data, dest_data):
    points = read_two_camera_points(src_data)

    camera1_point5 = get_hidden_point_from_ids(points, [4, 8, 6, 2, 1, 4, 3, 2, 1, 8], 0)
    camera2_point5 = get_hidden_point_from_ids(points, [4, 8, 6, 2, 1, 4, 3, 2, 1, 8], 1)
    
    camera1_point13 = get_hidden_point_from_ids(points, [10, 9, 11, 12, 10, 14, 11, 15, 14, 9], 0)
    camera2_point13 = [1077, 269, 1]

    camera1_point16 = get_hidden_point_from_ids(points, [10, 14, 11, 15, 10, 9, 11, 12, 12, 15], 0)
    camera2_point16 = get_hidden_point_from_ids(points, [10, 14, 11, 15, 10, 9, 11, 12, 12, 15], 1)

    points[5] = [camera1_point5, camera2_point5]
    points[13] = [camera1_point13, camera2_point13]
    points[16] = [camera1_point16, camera2_point16]

    save_points(points, dest_data)
