from elftools.elf.elffile import ELFFile


def find_padding(binary_path):
    binary = open(binary_path, 'rb')
    padding_size = get_padding_size(binary)
    binary_contents = binary.read()


def get_padding_size(binary):
    """ 
        Finds padding size by formula: e_shoff + (e_shentsize * e_shnum)
        Refer to the man page for more info: https://man7.org/linux/man-pages/man5/elf.5.html 
    """
    elffile = ELFFile(binary)
    parsed_header = elffile._parse_elf_header()
    e_shoff = parsed_header['e_shoff']
    e_shentsize = parsed_header['e_shentsize']
    e_shnum = parsed_header['e_shnum']
    return (e_shoff + (e_shentsize * e_shnum))
    