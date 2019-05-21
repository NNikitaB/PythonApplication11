class Comment:

    def __init__(self,user):
        self.text = ""
        self.comments=[]
        self.user=user

    def __init__(self,text,user):
        self.text = text
        self.comments=[]
        self.user=user

    def __init__(self, text, com ,user):
        self.text = text
        self.comments = [] + com
        self.user=user

    def Change(self,text):
        self.text=text

    def Add_Coment(self,text,user):
        self.comments.append(Comment(text,user))

    def get_owner(self):
        return self.user

    def get_text(self):
        return self.text

class Post:

    def __init__(self,user):
        self.listcomit =[]
        silf.text=""
        self.user=user

#комент и список сообщений
    def __init__(self, text , comit,user):
        self.listcomit =[] + comit 
        silf.text=text
        self.user=user
#post
    def __init__(self, text,user ):
        self.listcomit =[]
        silf.text=text
        self.user=user

    def get_text(self):
        return self.text

    def get_owner(self):
        return self.user

    def Add_Coment(self,text,user):
        self.listcomit.append(Comment(text,user))
    
#рекурсивный список сообщений под постом и коментов под сообщениями
    def Print_Post(self,f):
        if (len (self.listcomit) ==0):
            f.write(self.user)
            f.write(self.text)
            return
        for i in self.listcomit:
            i.comments



class Blog:

    def __init__(self):
        self.listpost =[]
        self.listname=[]

    def __init__(self,list):
        self.listpost =[]
        self.listname=[]+list

    def Add_User(self,user):
        self.listname.append(user)

    def FileSave(self,text):
        if (len(self.listpost) == 0):
            if (len(self.listname.count() ) == 0):
                return -1
        f = open(text, 'r+w')
        f.write(self.listname.count() + '\n')
        for i in self.listname:
            f.write(i,'\n')
        f.write(self.listpost.count() + '\n')
        for i in self.listpost:
            f.write(i.get_owner() + '\n' ) 
            f.write(i.text)#текст поста 
            #Текст сообщения



def main():
    print("LOL")



if __name__ == "__main__":
    main()