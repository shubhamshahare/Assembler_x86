f1 = open('directives.dat','r')
f2 = open('directives.h','w')
l  =  f1.readlines()
f2.write("struct directives{\n")
f2.write("  char *directive_name;\n")
f2.write("};\n")
f2.write("typedef struct directives directives;\n")
token1 = map(lambda x:x.rstrip(),l)
token2 = map(lambda x:x.split(),token1)
f2.write("#define MAX_DIRECTIVE_COUNT %d\n" %len(token2))
f2.write("directives directive_set[MAX_DIRECTIVE_COUNT]={")
for i in range(0,len(token2)-1):
  f2.write("{\""+token2[i][0]+"\"},")
f2.write("{\""+token2[len(token2)-1][0]+"\"}};")

