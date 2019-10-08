import io

offset0 = 0x4000
offset1 = 0x5000
offset2 = 0x5F4000
offset3 = 0x78A000
offset4 = 0x7B8000
offset5 = 0xDA7000

def dipper_maker(logo, fastboot, charging, logo2, corrupt, output):

	# Write file to output
	outpt = open(output, "wb")
	emptyContent =  [0 for i in range(0x1396000)]
	magic = [0x4C, 0x4F, 0x47, 0x4F, 0x21, 0x21, 0x21, 0x21, 0x05, 0x00, 0x00, 0x00,
	         0xEF, 0x05, 0x00, 0x00, 0xF4, 0x05, 0x00, 0x00, 0x96, 0x01, 0x00, 0x00,
	         0x8A, 0x07, 0x00, 0x00, 0x2E, 0x00, 0x00, 0x00, 0xB8, 0x07, 0x00, 0x00,
	         0xEF, 0x05, 0x00, 0x00, 0xA7, 0x0D, 0x00, 0x00, 0xEF, 0x05, 0x00, 0x00]

	# Write header file
	outpt.write(bytearray(emptyContent))
	outpt.seek(offset0)
	outpt.write(bytearray(magic))

	# Write boot logo image
	outpt.seek(offset1)
	img = open(logo, "rb")
	outpt.write(img.read())

	# Write fastboot logo image
	outpt.seek(offset2)
	img = open(fastboot, "rb")
	outpt.write(img.read())

	# Write charging logo image
	outpt.seek(offset3)
	img = open(charging, "rb")
	outpt.write(img.read())

	# Write boot logo unlocked image
	outpt.seek(offset4)
	img = open(logo2, "rb")
	outpt.write(img.read())

	# Write corrupt logo image
	outpt.seek(offset5)
	img = open(corrupt, "rb")
	outpt.write(img.read())

	# Close file
	outpt.close()

	return 1
