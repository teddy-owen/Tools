import os
import csv
import errno
import json

################################################################################
def get_dict_attributes(record_dict):
	'''
	take in dict of records and return 
	dict of list by attributes

	(dict)->dict
	'''
	attr_dict = {}
	for record in record_dict.keys():
		for attr in record_dict[record].keys():
			if attr in attr_dict:
			 	attr_dict[attr] += [record_dict[record][attr]]
			else:
				attr_dict[attr] = []
	return attr_dict

################################################################################

def filter_dict(record_dict,filters):
	'''
	take in dict of records and return 
	dict filtered on some attribute

	(dict)->dict

	e.g. filter1={"filter":"is","field":"country_code","values":["US","CA","UK"]}
	params: filter, field, values
	filter: is, is_not
	field:
	values:
	'''

	new_dict = {}

	# for each filter
	for record_filter in filters:
		filter_type = record_filter["filter"]
		field = record_filter["field"]
		values = record_filter["values"]

		for key_2, record in record_dict.items():
			curr_value = record[field]
			if ((filter_type == "is") and (curr_value in values)):
				new_dict[key_2] = record

			elif ((filter_type == "is_not") and (curr_value not in values)):
				new_dict[key_2] = record
		
		# update dict for next filter pass
		record_dict = new_dict

	return new_dict

################################################################################

def csv_to_dict(filename=None, has_header=True):
	'''
	converts csv into a dict (key = record)
	(str)->dict
	'''

	# import csv file "file_name" into model
	path = find_data_file(filename)

	csv_dict = {}
	with open(path, 'rt', encoding='utf-8') as f:
		reader = csv.reader(f)

		# either takes header or makes numerical header
		if has_header:
			header = next(reader)
		else:
			fields = len(next(reader))
			header = [x for x in range(fields)]
			f.seek(0) 

		i=0
		for row in reader:

			csv_dict[i] = {}

			j=0
			for item in row:
				curr_field = header[j]
				csv_dict[i][curr_field] = item
				j+=1

			i+=1
	
	return csv_dict

################################################################################

def find_data_file(filename=None):
	'''
	(str of filename) -> str of path to file
	searches for file in dir "data" or in . 
	order: [ . , .. , ../.. , . ]
	'''

	curr_path = os.path.abspath(os.path.join('.', 'data',filename))
	if (os.path.exists(curr_path)):
		return curr_path
	else:
		curr_path = os.path.abspath(os.path.join('..', 'data',filename))
		if(os.path.exists(curr_path)):
			return curr_path
		else:
			curr_path = os.path.abspath(os.path.join('..', '..', 'data',filename))
			if(os.path.exists(curr_path)):
				return curr_path
			else:
				curr_path = os.path.abspath(os.path.join('.',filename))
				if(os.path.exists(curr_path)):
					return curr_path
				else:
					raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)
	
	return

################################################################################
