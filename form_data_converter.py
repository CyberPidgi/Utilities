def remove_newline(string: str) -> str:
	return (string.rstrip('\n')).strip()


def convert_filedata_to_json(file):
	json_data = {}
	with open(file, 'r') as f:
		for line in map(remove_newline, f.readlines()):
			for index, char in enumerate(line):
				if char != ':':
					continue
				key, value = line[:index], line[index+1:]
				json_data[key.strip()] = value.strip()
				break

	return json_data


def main():
	file = r"YOUR PATH HERE"
	print(convert_filedata_to_json(file))


if __name__ == '__main__':
	main()
