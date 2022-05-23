def read(name):
    prefix = "traces\\"
    suffix = ".trace"
    filename = prefix + name + suffix
    file = open(filename,"r")
    contents = file.readlines()
    file.close()

    edited_contents = []
    length = len(contents)
    for ii in range(0,length):
        current_string = contents[ii]
        new_string = current_string[2:13]
        edited_contents.append(new_string)
    return edited_contents
