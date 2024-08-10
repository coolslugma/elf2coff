from elftools.elf.elffile import ELFFile

def read_elf(filename):
    with open(filename, 'rb') as f:
        elf = ELFFile(f)

        print("ELF Header:")
        for key, value in elf.header.items():
            print(f"{key}: {value}")

        print("\nSections:")
        for section in elf.iter_sections():
            print(f"Name: {section.name}, Type: {section['sh_type']}, Size: {section['sh_size']}")

        print("\nSegments:")
        for section in elf.iter_sections():
            print(f"Type: {segment['p_type']}, Size: {segment['p_filesz']}")

        return elf

def write_coff(elf, output_filename):
    with open(output_filename, 'wb') as f:
        # Currently, we have a stub. TODO: Write COFF header writing routines.
        coff_header = bytearray(20)  # COFF header is 20 bytes in a real file
        f.write(coff_header)

        # Write sections.
        for section in elf.iter_sections():
            f.write(section.data())

        print(f"COFF binary written to {output_filename}")

def convert_elf_to_coff(input_filename, output_filename):
    elf = read_elf(input_filename)
    write_coff(elf, output_filename)

input_elf_file = 'example.elf'
output_coff_file = 'example.coff'

convert_elf_to_coff(input_elf_file, output_coff_file)