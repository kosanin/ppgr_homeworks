import numpy as np
import operator
import functools


def save_points(points, path):
    with open(path, "w+") as f:
        for k, v in points.items():
            flattened_list_of_points = functools.reduce(operator.concat, v)
            f.write(str(k) 
                    + functools.reduce(lambda acc, val: acc + " " + str(val), flattened_list_of_points, "")
                    + "\n")


def get_hidden_point_from_ids(points, ids, camera_flag):
    """
    :param points: map
    :param ids: list
        lista id-va tacaka koje ucestvuju u dobijanju koordinata skrivene tacke.
        prva dva id-a(id[0] i id[1]) predstavljaju kolinearne tacke, ciji vektor se sece
        u tacki nedogleda sa vektorom tacaka id[2] i id[3]; analogno za sledeca 4 id-a
        poslednja dva id-a predstavljaju tacke koje medjusobno nisu kolinearne,
        ali su kolinearne sa skrivenom tackom. presek prava 
        id[8] x tacka_nedogleda1 
        id[9] x tacka_nedogleda2 daju skrivenu tacku
    :param camera_flag: int
    """
    x_inf = vanishing_point(points[ids[0]][camera_flag],
                            points[ids[1]][camera_flag],
                            points[ids[2]][camera_flag],
                            points[ids[3]][camera_flag])
    
    y_inf = vanishing_point(points[ids[4]][camera_flag],
                            points[ids[5]][camera_flag],
                            points[ids[6]][camera_flag],
                            points[ids[7]][camera_flag])
    
    colinear_point1 = points[ids[8]][camera_flag]
    colinear_point2 = points[ids[9]][camera_flag]

    return hidden_point(colinear_point1, x_inf,
                        colinear_point2, y_inf).tolist()


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


def hidden_point(colinear_pt1, vanishing_pt1,
                 colinear_pt2, vanishing_pt2):
    """

    :param colinear_pt1:
    :param vanishing_pt1:
        colinear_pt1 i vanishing_pt1 pripadaju istoj pravi
    :param colinear_pt2:
    :param vanishing_pt2:
        colinear_pt2 i vanishing_pt2 pripadaju istoj pravi
    :return:
    """
    hidden_pt = np.cross(
        np.cross(colinear_pt1, vanishing_pt1),
        np.cross(colinear_pt2, vanishing_pt2)
    )
    return to_affine_coordinates(hidden_pt)


def vanishing_point(line1_pt1, line1_pt2,
                 line2_pt1, line2_pt2):

    line1 = np.cross(line1_pt1, line1_pt2)
    line2 = np.cross(line2_pt1, line2_pt2)
    vanishing_point1 = np.cross(line1, line2)

    return vanishing_point1


def triangulation(points, fund_matrix):

    camera1, camera2 = get_cameras_matrices(fund_matrix)

    reconstructed_3d_coordinates = []
    for cam1_pt, cam2_pt in points.values():
        reconstructed_3d_coordinates.append(
                    to_affine_coordinates(
                    reconstruct_point_coordinates(cam1_pt, cam2_pt, camera1, camera2))
                    # drop last coordinate
                    [:-1].tolist())

    return reconstructed_3d_coordinates


def reconstruct_point_coordinates(camera1_pt, camera2_pt, camera1, camera2):

    # TODO REFAKTORISATI, ZASTO mora za camera2 .tolist()[0] ?
    linear_system = [
        (np.dot(camera1_pt[1], camera1[2, :]) - camera1[1, :]).tolist(),
        (-np.dot(camera1_pt[0], camera1[2, :]) + camera1[0, :]).tolist(),
        (np.dot(camera2_pt[1], camera2[2, :]) - camera2[1, :]).tolist()[0],
        (-np.dot(camera2_pt[0], camera2[2, :]) + camera2[0, :]).tolist()[0]
    ]

    _, _, v = np.linalg.svd(linear_system, full_matrices=True)
    return v[v.shape[0] - 1]


def vector2mult_matrix(vec):

    return [[0, -vec[2], vec[1]],
            [vec[2], 0, -vec[0]],
            [-vec[1], vec[0], 0]]


def get_cameras_matrices(fund_matrix):

    camera1 = np.append(np.identity(3), np.array([0, 0, 0]).reshape(3, 1), axis=1)

    _, e2 = epipoles(fund_matrix)
    e2_mult_matrix = vector2mult_matrix(to_affine_coordinates(e2))
    camera2 = np.dot(e2_mult_matrix, fund_matrix)
    camera2 = np.append(camera2, np.array(to_affine_coordinates(e2)).reshape(3, 1), axis=1)

    return camera1, camera2


def to_affine_coordinates(homogeneous_point):
    # return list(map(int, (homogeneous_point * (1 / homogeneous_point[len(homogeneous_point) - 1]))))
    w = homogeneous_point[-1]
    return np.multiply(1/w, homogeneous_point)


def epipoles(fund_matrix):

    u, _, v = np.linalg.svd(fund_matrix, full_matrices=True)

    # pogledati materijale sa predavanja
    # v[2] vraca np.matrix, pa ga razmotavamo u listu sa tolist()[0]
    camera1_epipole = v[2, :].tolist()[0]
    camera2_epipole = u[:, 2].ravel().tolist()[0]
    return camera1_epipole, camera2_epipole


def normalized_fundamental_matrix(fund_matrix):
    """
    normalizacija fundamentalne matrice radi postizanja uslova
    det(fund_matrix) = 0
    """
    u, d, v = np.linalg.svd(fund_matrix, full_matrices=True)
    # pogledati predavanja (Zisserman)
    d[-1] = 0.0
    return np.linalg.multi_dot([u, np.diag(d), v])


def fundamental_matrix(camera1_pts, camera2_pts):
    corr_matrix = correspondance_matrix(camera1_pts, camera2_pts)
    fundamental_mat = dlt(corr_matrix)
    if is_fundamental_matrix(fundamental_mat, camera1_pts, camera2_pts):
        return fundamental_mat
    else:
        # TODO refaktorisati
        return []


def is_fundamental_matrix(matrix, camera1_pts, camera2_pts):

    for x, y in zip(camera1_pts, camera2_pts):
        if not np.allclose(np.linalg.multi_dot([y, matrix, x]), 0):
            return False

    return True


def dlt(mat):

    _, _, v = np.linalg.svd(mat, full_matrices=True)

    # uzimmo poslednju vrstu
    last_row = v.shape[1] - 1
    dlt_matrix = list(v[last_row])

    dlt_matrix = [dlt_matrix[i:i + 3] for i in range(0, len(dlt_matrix), 3)]
    return np.matrix(dlt_matrix)


def correspondance_matrix(camera1_pts, camera2_pts):
    ceofs = []
    for corresponding_pts in zip(camera1_pts, camera2_pts):
        ceofs.append(corresponding_pts_relation(corresponding_pts[0], corresponding_pts[1]))

    return ceofs


def corresponding_pts_relation(first_camera_pixel, second_camera_pixel):
    # y.Tranpose F x = 0
    tmp = []
    for snd_camera_coordinate in second_camera_pixel:
        for fst_camera_coordinate in first_camera_pixel:
            tmp.append(fst_camera_coordinate * snd_camera_coordinate)

    return tmp


def read_two_camera_points(path):
    # linija fajla koji citamo je
    # id c1_x c1_y c1_w c2_x c2_y c2_w
    points = {}
    with open(path) as f:
        for line in f.readlines():
            data = list(map(float, line.split()))
            id = data[0]
            first_camera_point_coordinates = data[1:4]
            second_camera_point_coordinates = data[4:7]
            points[id] = [first_camera_point_coordinates, second_camera_point_coordinates]
    return points


def main():
    slika1("data/tmp.txt", "data/slika1.txt")


if __name__ == '__main__':
    main()
