def missing_char(str, n):
  if n in range(len(str)):
    return str.replace(str[n],"")
