print("Alfaro Ibarra Sheccid,3w, 1171")
#"w"- Escribir: sobrescribirá cualquier contenido existente
f6 = open("demofile3.txt", "w")
f6.write("Woops! I have deleted the content!")
f6.close()

#abrir y leer el archivo después de sobrescribirlo:
f6 = open("demofile3.txt", "r")
print(f6.read())
