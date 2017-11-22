# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):

  page_dict = {}
  for i in range(0,len(site_list)):
      if site_list[i] in page_dict:
          page_dict[site_list[i]].add(user_list[i])
      else:
          page_dict[site_list[i]] = {user_list[i]}     # use set
# print(page_dict)

  dict_keys = list(page_dict.keys())
# print(dict_keys)

  maxLen = 0;
  for i in range(0,len(dict_keys)):
      for j in range(i+1,len(dict_keys)):
          intersec = page_dict[dict_keys[i]] & page_dict[dict_keys[j]]
          if(len(intersec)>maxLen):
              maxLen = len(intersec)
              result = (dict_keys[i],dict_keys[j])
  if result[0]<result[1]:
      return (result[0],result[1])
  else:
      return (result[1],result[0])


      

  page_dict = {}
  for i in range(0,len(site_list)):
      if site_list[i] in page_dict:
          page_dict[site_list[i]].add(user_list[i])
      else:
          page_dict[site_list[i]] = {user_list[i]}     # use set
# print(page_dict)

  dict_keys = list(page_dict.keys())
  page_dict = {}
  for i in range(0,len(site_list)):
      if site_list[i] in page_dict:
          page_dict[site_list[i]].add(user_list[i])
      else:
          page_dict[site_list[i]] = {user_list[i]}     # use set
# print(page_dict)

  dict_keys = list(page_dict.keys())  
  page_dict = {}
  for i in range(0,len(site_list)):
      if site_list[i] in page_dict:
          page_dict[site_list[i]].add(user_list[i])
      else:
          page_dict[site_list[i]] = {user_list[i]}     # use set
# print(page_dict)

  dict_keys = list(page_dict.keys())

