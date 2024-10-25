print("Alfaro Ibarra Sheccid,3w, 1171")
#Para evitar obtener un error, es posible que desees
#verificar si el archivo existe antes de intentar eliminarlo:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")