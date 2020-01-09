import numpy as np


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
    return np.cross(
        np.cross(colinear_pt1, vanishing_pt1),
        np.cross(colinear_pt2, vanishing_pt2)
    )


def vanishing_point(line1_pt1, line1_pt2,
                 line2_pt1, line2_pt2):

    line1 = np.cross(line1_pt1, line1_pt2)
    line2 = np.cross(line2_pt1, line2_pt2)
    vanishing_point1 = np.cross(line1, line2)

    return vanishing_point1


def triangulation(camera1_pts, camera2_pts):

    fund_matrix = fundamental_matrix(camera1_pts, camera2_pts)
    camera1, camera2 = get_cameras_matrices(fund_matrix)

    reconstructed_3d_coordinates = []
    for cam1_pt, cam2_pt in zip(camera1_pts, camera2_pts):
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

    u, v, d = np.linalg.svd(linear_system, full_matrices=True)
    return d[d.shape[0] - 1]


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
    return homogeneous_point * (1 / homogeneous_point[len(homogeneous_point) - 1])


def epipoles(fund_matrix):

    u, d, v = np.linalg.svd(fund_matrix, full_matrices=True)

    # pogledati materijale sa predavanja
    # v[2] vraca np.matrix, pa ga razmotavamo u listu sa tolist()[0]
    camera1_epipole = v[2, :].tolist()[0]
    camera2_epipole = u[:, 2].ravel().tolist()[0]
    return camera1_epipole, camera2_epipole


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

    u, d, v = np.linalg.svd(mat, full_matrices=True)

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
            data = list(map(int, line.split()))
            id = data[0]
            first_camera_point_coordinates = data[1:4]
            second_camera_point_coordinates = data[4:7]
            points[id] = [first_camera_point_coordinates, second_camera_point_coordinates]
    return points


def main():
    pass


if __name__ == '__main__':
    main()
