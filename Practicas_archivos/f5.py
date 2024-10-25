print("Alfaro Ibarra Sheccid,3w, 1171")
#Para escribir en un archivo existente, debe agregar un parámetro a la open()función:
#"a"- Anexar - se agregará al final del archivo
t5 = open("demofile2.txt", "a")
t5.write("Now the file has more content!")
t5.close()

#abre y lee el archivo después del adjunto:
tu5 = open("demofile2.txt", "r")
print(tu5.read())