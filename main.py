from exif import Image
import glob
import shutil
import os
import time

#shutil.copy2('myFile', 'myFile2') : comme shutil.copy, mais en plus recopie les permissions et les dates de dernier accès et de modification (similaire à la commande linux "cp -p").

#img_path = './DSCN0279.JPG'
#with open(img_path, 'rb') as src:
#    img = Image(src)
#    print(img.get("datetime_original"))

directorySource = 'X:\PhotosTrie\A FAIRE'
directoryDest = 'X:\PhotosTrie'
directoryDestVideo = 'X:\PhotosTrie\Videos'

NbFic = 0
NombreFichierRenomer = 0
NombreFichierCopier = 0
NbIdentique = 0
for path in glob.iglob(f'{directorySource}/**/*.jpg', recursive=True):
    NbFic = NbFic + 1
    ImageValide = True
    print(str(NbFic) + " " + path)
    OldName = path.split("\\")[-1]
    with open(path, 'rb') as src:
        try: 
            img = Image(src)
            if ("datetime_original" in img.list_all()):
                DateTime = img.get("datetime_original") 
            else:
                DateTime = time.strftime('%Y:%m:%d %H:%M:%S', time.gmtime(os.path.getmtime(path)))
        except:
            print("Value ERROR */******************************************")
            DateTime = time.strftime('%Y:%m:%d %H:%M:%S', time.gmtime(os.path.getmtime(path)))
#    print("_" + DateTime + "_")
    if not (":" in DateTime):
        DateTime = time.strftime('%Y:%m:%d %H:%M:%S', time.gmtime(os.path.getmtime(path)))
#    print("_" + DateTime + "_")

    NvNom = DateTime.split(" ")[0].replace(":","-") + "_" + DateTime.split(" ")[1].replace(":","")
    NvRepRacine = DateTime.split(":")[0]
    NbRepN2  = DateTime.split(":")[0] + "-" +  DateTime.split(":")[1] 
#    print(path + " " +  NvNom + " " + NvRepRacine + " " + NbRepN2)
    
    if not os.path.exists(directoryDest + '\\' + NvRepRacine):
        os.makedirs(directoryDest + '\\' + NvRepRacine)
    if not os.path.exists(directoryDest + '\\' + NvRepRacine + '\\' + NbRepN2):
        os.makedirs(directoryDest + '\\' + NvRepRacine + '\\' + NbRepN2)
    
    NewFile=directoryDest + "\\" + NvRepRacine + "\\" + NbRepN2 + "\\" + NvNom  + "_" + OldName

#    print(NewFile)
    if glob.glob(NewFile): #verfiie si fichier existe déja
#        print("Fichier EXIST:" + path)
        
        if os.stat(NewFile).st_size == os.stat(path).st_size:
           NbIdentique += 1
           NewFile = "IDENTIQUE"
           print("Existe Deja => Ranger")
           #shutil.move(path, "X:\\PhotosTrie\\Existe\\" +  NvNom  + "_" + str(NbIdentique) + "_" + OldName ) 
           os.remove(path)
        else:
           NewFile = ""
           for NumFic in range(2000):
               if glob.glob(directoryDest + "\\" + NvRepRacine + "\\" + NbRepN2 + "\\" + NvNom  + "_" + str(NumFic) + "_" + OldName):
                  if os.stat(directoryDest + "\\"  + NvRepRacine + "\\" + NbRepN2 + "\\" + NvNom  + "_" + str(NumFic) + "_" + OldName).st_size == os.stat(path).st_size:
#                       print("2 taille identique: " + path + " " + "X:\\PhotosTrie\\" + NvRepRacine + "\\" + NbRepN2 + "\\" + NvNom  + "_" + str(NumFic) + ".JPG")
                       NewFile = "IDENTIQUE"
                       break 
               else:
                   NewFile = directoryDest + "\\"  + NvRepRacine + "\\" + NbRepN2 + "\\" + NvNom  + "_" + str(NumFic) + "_" + OldName
                   break

           if (NewFile == ""):
              print("ERREUR2: "  + path)
              break
           elif (NewFile != "IDENTIQUE"):
               shutil.move(path, NewFile) 
           else:
                print("Existe Deja => Ranger")
#                shutil.move(path, "X:\\PhotosTrie\\Existe\\" +  NvNom  + "_" + str(NbIdentique) + "_" + OldName ) 
                os.remove(path)
    else:
        shutil.move(path, NewFile)

