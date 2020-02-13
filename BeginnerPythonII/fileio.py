
def copy_binary(infile, outfile, inmode='rb', outmode='ab'):
    buf_len = 10240
    count = 0
    with open(infile, inmode) as ifn:
        with open(outfile, outmode) as ofn:

            while True:
                buf = ifn.read(buf_len)
                if buf:
                    ofn.write(buf)
                else:
                    break
                if count >= 5:
                    break
                count += 1


def main():

    # Read a binary file, and write it to a different file.
    # *****************************
    # *****************************

    injpg = 'noaalogo.jpg'
    ofile = 'noaalogo_partial.jpg'
    copy_binary(injpg, ofile, outmode='wb')

    # Write and read a text file.
    # *****************************
    # *****************************
    names = ['bob', 'john', 'jill', 'katie', 'annie']

    # ---------------------------------------------------------------------------------------
    # The python "with" statement encapsulates common prep/cleanup tasks in context managers.
    # Especially useful for opening files, file locking, database connections, etc. 
    # The following example with "open" would otherwise look like this:
    #
    #         fn = open(ofile, 'w')
    #         for .....:
    #             fn.write(....)
    #         fn.close()
    #
    # The user is left to close the file.
    #
    # ---------------------------------------------------------------------------------------

    ofile = 'names.txt'
    with open(ofile, 'w') as fn:
        for i, item in enumerate(names):
            fn.write(' '.join([str(i), item, '\n']))

    with open(ofile, 'r') as fn:
        lines = fn.readlines()

    for line in lines:
        print(line)

    # Parse contents of text file into list
    contents_list = []
    for line in lines:
        contents_list.append(line.rstrip().split())

    print(f"List with loop: {contents_list}")
    # Use a list comprehension instead
    alt_content = [line.rstrip().split() for line in lines]
    print(f"List with comp: {alt_content}")

    # Parse contents of text file into a dict1
    content_dict = {k: v for k, v in [line.rstrip().split() for line in lines]}

    print(f"Dict with comp: {content_dict}")

if __name__ == '__main__':
    main()


