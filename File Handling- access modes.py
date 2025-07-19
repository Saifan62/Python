file = open("Saifan's lifestyle.txt", 'r')
Counter = 0
Content= file.read()
Colist = Content.split('\n')
for i in Colist:
    if i:
        Counter += 1
print("This is the number of lines in the file:")
print(Counter)
file.close()

file_write = open("Saifan's lifestyle.txt", 'w')
print("File opened in write mode:")
file_write.write("Saifan is my best friend. His Minecraft name is SaifanBrine.")
file_write.close()

file_append = open("Saifan's lifestyle.txt", 'w')
print("File opened in write mode:")
file_append.write("And me, I am his best friend my name is Arhaan. I am a c++ developer.My minecraft name is ZephyrV2.") 

file_append.close()
