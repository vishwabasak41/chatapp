from defaults import SPY_LIST
from time import gmtime, strftime
from steganography.steganography import Steganography
choice = 1
choose='Y'
MSG={}
chat_name=[]
chat_msg=[]
chat_time=[]
STATUS=['Hi All','NEW SPACE','Nerdy!']







while choice==1:
    choose=raw_input("Do you wish to enter as a new spy:(Y/N)")
    if choose =='Y':
        print "Welcome to the chatting site"
        user_name=raw_input("What's your name?")
        if user_name in SPY_LIST.keys():
            print "Already existing"
            continue
        else:
            print "Hii!"
            spyname=raw_input("Enter your name again!")
            spy_age=int(raw_input("Enter your age"))
            spy_rate=(raw_input("Enter your rate"))
            SPY_LIST[spyname]={
                "spy age":spy_age,
                "spy rate":spy_rate
            }

            while choice != 6:
                def add_status(self):
                    choice_status = raw_input("Do you wish to add from \n1. previous status or\n2.gt a new one?")
                    if choice_status == '1':
                        status_inp = int(raw_input("Enter any number between 0-2"))
                        SPY_LIST[spyname]['status'] = STATUS[status_inp]
                        print SPY_LIST
                    elif choice_status == '2':
                        stat=raw_input("Enter a new status")
                        SPY_LIST[spyname]['Status']=stat
                        print "spy list is",SPY_LIST
            #MENU

                print "1.for adding your status \n 2.for addind a friend \n3.for sending ecrypted message \n 4.for reading decrypted message \n 5.for reading previous chats \n 6. or quiting"
                user_wish=raw_input("Pick any one of the following choices-")



                #adding status  f

                if user_wish=='1':
                    print "You wish to add a Status.Granted!"


                    add_status(spyname)






                #adding friends
                elif user_wish=='2':
                    i=0
                    SPY_FRIENDS={}
                    friend_namelist = []
                    friend_agelist=[]
                    friend_ratelist=[]
                    ch=True
                    print"You wish to add a Friend.Granted!"
                    frend_no=raw_input("Enter No of Friends")
                    while i<int(frend_no):
                        print "i",i
                        frend_name = raw_input("Enter Name of Friends")
                        frend_age = int(raw_input("Enter your age"))
                        frend_rate = (raw_input("Enter your rate"))
                        friend_namelist.append(frend_name)
                        friend_agelist.append(frend_age)
                        friend_ratelist.append(frend_rate)
                        SPY_FRIENDS={
                            "name of spy":spyname

                        }
                        spyname={
                            "Friend names":friend_namelist,
                            "Friend age":friend_agelist,
                            "Friend rate":friend_ratelist
                        }

                        print spyname
                        print SPY_FRIENDS
                        print SPY_FRIENDS.keys()
                        i=i+1

                elif user_wish == '3':
                    msg_to_frendname=raw_input("which friend do you wish to send?")
                    if msg_to_frendname in spyname["Friend names"]:
                        pic_path=raw_input("Enter path for the pic")
                        pic_name=raw_input("Enter name of pic with extension")
                        pic_inp=pic_path+pic_name
                        print pic_inp
                        pic_op="/home/vishwarupa/Documents/pic_op_path/"
                        pic_op_name=raw_input("Enter pic output name with extension")
                        pic_op_path=pic_op+pic_op_name
                        msg=raw_input("Enter text you wish to hide")
                        Steganography.encode(pic_inp,pic_op_path,msg)
                        print "Encoded!"


                    else:
                        print "Friend Offline"



                elif user_wish == '4':
                    spyname_msg=spyname
                    pic_op = "/home/vishwarupa/Documents/pic_op_path/"
                    pic_op_name = raw_input("Enter pic output name with extension")
                    pic_op_path = pic_op + pic_op_name
                    print pic_op_path
                    msg_was=Steganography.decode(pic_op_path)
                    print "Your message is:",msg_was
                    time_is=strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    print time_is
                    chat_name.append(msg_to_frendname)
                    chat_msg.append(msg)
                    chat_time.append(time_is)
                    MSG_FRIENDS = {
                        "name of spy": spyname_msg

                    }
                    spyname_msg = {
                        "Friend's names": chat_name,
                        "Friend message to you": chat_msg,
                        "Time": chat_time
                    }
                    print "spyname_msg",spyname_msg
                    print MSG_FRIENDS

















