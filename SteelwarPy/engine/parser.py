#Gnurilla Parser
#by Otacon22

#note per lo sviluppatore:
#avviare il controllo dell' integirta' utilizzando la funzione ceck_integrity dando come argomento di init il file da analizzare,
#allo stesso modo estrarre variabili da file dando sempre come argomento di init il file.
#esempi:
#import parser
#...
#parser.Parser("File.ext").ceck_integrity()
#...
#print parser.Parser("File.ext").get_vars()
#
#Errors can return with "Error" with not valid file or "Error Exist" if the file don't exist



class Parser:
    def __init__(self, FileDict):
        self.File=FileDict
        self.ClassSeparator=":"
        self.ObjDefinition="=" #don't use space!

    def openfile(self, file):
        try:
            file_=open(file, "r")
            data=file_.read()
            file_.close()
        except:
            data="Error"
        return data
    def ceck_integrity(self):
        data=self.openfile(self.File)
        if data!="Error0":
            for line in data.split("\n"):

                if line=="" or line=="\n":
                    pass
                else:
                    if "".join("".join(line.split(" ")).split("\t"))[0]!="#":
                        if len(line.split(self.ObjDefinition))==2:
                            if "".join("".join(line.split(self.ObjDefinition)[0].split(" ")).split("\t"))=="":
                                return "Error1"
                            elif "".join("".join(line.split(self.ObjDefinition)[0].split(" ")).split("\t")).split("#")==2:
                                return "Error2"
                        elif len(line.split(self.ClassSeparator))==2:
                            if line.split(self.ClassSeparator)[0]=="":
                                return "Error3"
                        else:
                            return "Error4"
                        
                    
        else:
            return "Error Exist"
        
        return "Ok"
    
    def extractvars(self, data):
        dict={}
        lastclass=""
        for line in data.split("\n"):
            if line=="" or line=="\n":
                pass
            elif "".join(line.split(" "))[0]=="#":
                pass
            elif len(line.split(self.ClassSeparator))==2:
                lastclass="".join("".join(line.split(self.ClassSeparator)[0].split(" ")).split("\t")) 
                if not dict.has_key(lastclass):
                    dict[lastclass]={}
            elif len(line.split(self.ObjDefinition))==2:
                if lastclass=="":
                    dict["".join("".join(line.split(self.ObjDefinition)[0].split(" ")).split("\t"))]="".join("".join(line.split(self.ObjDefinition)[1].split(" ")).split("\t")).split("#")[0]
                else:
                    dict[lastclass]["".join("".join(line.split(self.ObjDefinition)[0].split(" ")).split("\t"))]="".join("".join(line.split(self.ObjDefinition)[1].split(" ")).split("\t")).split("#")[0]

        return dict
    
    
    def get_vars(self):
        return self.extractvars(self.openfile(self.File))




    
        
            
            

        




