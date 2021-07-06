"""
This module creates a new PDDL file from the original.

 - Open the original PDDL problem file
 - Store its content in a list
 - Update this list from user inputs
 - Iterate over this updated list and write the list content in a new file
"""


def write_new_problem_file(path):
    """
    Read a list and write its content into a new file
    :param path: Absolute path for the output file
    :type path: str
    :return: None
    :rtype: None
    """
    with open(path, 'w') as writer:
        for item in output_list:
            # The indentation in the file needs some work but this is fine
            writer.write(item)


def read_file(path):
    """
    Open a file and store its content in a list
    :param path: Absolute path for the file to open
    :type path: str
    :return: List of each line of the file
    :rtype: List
    """

    with open(path, 'r') as opened_file:
        state_list = []
        lines = opened_file.readlines()

        for line in lines:
            state_list.append(line)
            # print(line)

        return state_list


def update_problem_states():
    """
    Read a list and update some of its contents from user inputs
    :return: None
    :rtype: None
    """
    agv_is_at_ks_counter = 0

    # ----------------------------
    # start data from user inputs
    # We assume the following information comes from user inputs
    # agv information
    used_agv = 'agv2'
    used_agv_station = 'as2'
    at_ks = ['agv1', 'agv3', 'agv4']

    # bin and part type information
    blue_battery_bin = 'bin2'
    red_battery_bin = 'bin5'
    blue_sensor_bin = 'bin4'
    green_regulator_bin = 'bin8'

    # end data from user inputs
    # ----------------------------

    # update predicates and attributes from user inputs
    for i in range(len(output_list)):
        if 'agv-is-at-as' in output_list[i]:
            output_list[i] = "(agv-is-at-as "+used_agv+" "+used_agv_station+")\n"
        if 'agv-is-not-at-ks' in output_list[i]:
            output_list[i] = "(agv-is-not-at-ks " + used_agv + ")\n"
        if 'agv-is-at-ks' in output_list[i]:
            if agv_is_at_ks_counter == 0:
                output_list[i] = "(agv-is-at-ks " + at_ks[agv_is_at_ks_counter]+")\n"
            elif agv_is_at_ks_counter == 1:
                output_list[i] = "(agv-is-at-ks " + at_ks[agv_is_at_ks_counter]+")\n"
            elif agv_is_at_ks_counter == 2:
                output_list[i] = "(agv-is-at-ks " + at_ks[agv_is_at_ks_counter]+")\n"
            agv_is_at_ks_counter += 1
        if 'bin-has-parttype' in output_list[i] and 'blue_sensor' in output_list[i]:
            output_list[i] = '(bin-has-parttype '+blue_sensor_bin+' blue_sensor)\n'
        if 'bin-has-parttype' in output_list[i] and 'green_regulator' in output_list[i]:
            output_list[i] = '(bin-has-parttype '+green_regulator_bin+' green_regulator)\n'
        if 'bin-has-parttype' in output_list[i] and 'blue_battery' in output_list[i]:
            output_list[i] = '(bin-has-parttype '+blue_battery_bin+' blue_battery)\n'
        if 'bin-has-parttype' in output_list[i] and 'red_battery' in output_list[i]:
            output_list[i] = '(bin-has-parttype '+red_battery_bin+' red_battery)\n'


if __name__ == '__main__':
    # absolute path to the PDDL problem file
    input_file_path = "/home/brenda/Desktop/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"
    # absolute path to the new PDDL problem file
    output_file_path = "/home/brenda/Desktop/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
    output_list = read_file(input_file_path)
    update_problem_states()
    write_new_problem_file(output_file_path)
