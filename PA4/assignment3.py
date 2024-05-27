import numpy as np
import sys
import ios
import methods
import Carthesian_math_package
import Q2

def pre_process_objects():

    body_file_a = "data/Problem3-BodyA.txt"
    body_file_b = "data/Problem3-BodyB.txt"
    mesh_file = "data/Problem3MeshFile.sur"
    body_a, tip_a = ios.loadbody(body_file_a)
    body_b, tip_b = ios.loadbody(body_file_b)
    vertices, triangles = ios.loadmesh(mesh_file)
    return body_a, tip_a, body_b, tip_b, vertices, triangles


def run_procedure(prefix, ftype, char, body_a, tip_a, body_b, vertices, triangles,
                  closest_point_mesh_function, tree=None):

    sample_readings_file = prefix+char+ftype+"-SampleReadingsTest.txt"
    a_matrix, b_matrix = ios.loadsamplereadings(sample_readings_file, body_a.shape[1], body_b.shape[1])
    d_matrix = np.empty((3, a_matrix.shape[2]))
    c_matrix = np.empty((3, a_matrix.shape[2]))
    tip_a = tip_a.reshape(-1, 1)
    for k in range(a_matrix.shape[2]):
        a = a_matrix[:, :, k]
        b = b_matrix[:, :, k]
        R_ak, p_ak = Q2.Registration(body_a, a)
        R_bk, p_bk = Q2.Registration(body_b, b)
        R_bk_inv, p_bk_inv = Carthesian_math_package.invert_transformation(R_bk, p_bk)
        d = Carthesian_math_package.transform(R_bk_inv, p_bk_inv, Carthesian_math_package.transform(R_ak, p_ak, tip_a))
        if tree is None:
            c = closest_point_mesh_function(triangles, vertices, d)
        else:
            c = closest_point_mesh_function(tree, d)
        d_matrix[:, k] = d.ravel()
        c_matrix[:, k] = c.ravel()
    return d_matrix, c_matrix


def main():

    np.set_printoptions(precision=2, suppress=True)
    if len(sys.argv) < 2:
        char = 'H'
    else:
        char = sys.argv[1]
    if not (char == "G" or char == "H" or char == "J"):
        char = 'H'
    prefix = "data/PA3-"
    ftype = "-Unknown"
    output_file = prefix+char+ftype+"-Output.txt"
    body_a, tip_a, body_b, tip_b, vertices, triangles = pre_process_objects()
    tree = methods.BuildOctree(vertices, triangles)
    d_matrix, c_matrix = run_procedure(prefix, ftype, char, body_a, tip_a, body_b, vertices, triangles,
                                       methods.ClosestPointOctree, tree)
    ios.write_output(output_file, d_matrix, c_matrix)
    return


if __name__ == '__main__':
    main()
