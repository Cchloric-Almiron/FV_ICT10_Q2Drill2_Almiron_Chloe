#Drill2 
from pyscript import document, display


def check_me(e):

    document.getElementById('results').innerHTML = "" #clear

    #list of names 
    grade7 = {"Acosta, Isabela", "Castillo, Eliza", "Francisco, Xian"}
    grade8 = {"Godino, Jadrien", "Llaguno, Zara", "Saludes, Rocky"}
    grade9 = {"Joven, Jarvis" , "Supangan, Zackery", "Gloria, Angelo"}

    #name of student
    firstName = document.getElementById('Fname').value
    lastName = document.getElementById('Lname').value
    new = lastName + "," + firstName
    newperson = {new}  

    #member list 
    all_members = grade7 | grade8 | grade9 | newperson
    members_list = " ".join(sorted(all_members))


    display(f"Members: <br> {members_list}", target = "output1")
    display(f"Amount of members: {len(members_list)}", target = "output1")

    

