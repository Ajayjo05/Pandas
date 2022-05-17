import re
str= '''INSERT INTO public.extractor_configs_old (id, "name", doc_type, valid_pages, source_page_resolution, "key_type", key_regex, key_position, key_level, value_type, value_data_type, value_regex, value_position, "dynamic", capture_regex, format_regex, config_set, top_limiter, bottom_limiter, left_limiter, right_limiter, confidence_score, capture_index, priority, enabled) VALUES(62, 'apn', 'Deed', 'all', 200, 'variable', '(?i)(Tax\sID[\W]*)', '931,704,1660,1304', 'line', 'text', 'string', '(?i)(?:Tax\sID[\W]*)(\w?[\-\d]+)', '931,704,1660,1304', false, '', '', 'Fluid', NULL, NULL, NULL, NULL, 70, -1, 4, true);'''
key = re.findall('(?i)(?:\(id\,\s)(.*?)(?=\)\svalues)', str)
val = re.findall('(?i)(?:values\([\d]+\,\s)(.*)(?=\;)', str) 
k=','.join(key)
v=','.join(val)
k=k.split()
v=v.split()
str1=''
for i in range(0,len(v)):
    if i!=len(v)-1:
        str1=str1+k[i]+"="+v[i]+" and "       
    else:
        str1=str1+k[i]+"="+v[i] + ";"
runner=re.sub('(?i)(\,=)',' = ',str1)
run=runner.replace(', ',' ')
str_table_name=re.search('(?i)(public.extractor_configs_old)(?=\s\()',str)
final= "UPDATE " +str_table_name[0]+" SET "+" where "+run

print(final)





